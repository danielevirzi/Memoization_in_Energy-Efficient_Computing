from EventManager.Models.RunnerEvents import RunnerEvents
from EventManager.EventSubscriptionController import EventSubscriptionController
from ConfigValidator.Config.Models.RunTableModel import RunTableModel
from ConfigValidator.Config.Models.FactorModel import FactorModel
from ConfigValidator.Config.Models.RunnerContext import RunnerContext
from ConfigValidator.Config.Models.OperationType import OperationType
from ProgressManager.Output.OutputProcedure import OutputProcedure as output
from typing import Dict, List, Any, Optional
from pathlib import Path
from os.path import dirname, realpath
import numpy as np
import sys
import os
import signal
import pandas as pd
import time
import subprocess
import shlex
import textwrap
import re
import math

class RunnerConfig:
    ROOT_DIR = Path(dirname(realpath(__file__)))

    # ================================ USER SPECIFIC CONFIG ================================
    """The name of the experiment."""
    name:                       str             = "dft_experiment"
    """target function location in remote laptop"""
    target_function_location = 'cpu.dft'
    target_function_names = ["DFT", "DFT_cache", "DFT_lru_cache"]
    input_size_options = [128, 256, 512]
    input_description = ["128 points", "256 points", "512 points"]
    sampling_rate_options = [50]

    """The path in which Experiment Runner will create a folder with the name `self.name`, in order to store the
    results from this experiment. (Path does not need to exist - it will be created if necessary.)
    Output path defaults to the config file's path, inside the folder 'experiments'"""
    results_output_path:        Path             = ROOT_DIR / 'experiments'

    """Experiment operation type. Unless you manually want to initiate each run, use `OperationType.AUTO`."""
    operation_type:             OperationType   = OperationType.AUTO

    """The time Experiment Runner will wait after a run completes.
    This can be essential to accommodate for cooldown periods on some systems."""
    time_between_runs_in_ms:    int             = 1000

    # Dynamic configurations can be one-time satisfied here before the program takes the config as-is
    # e.g. Setting some variable based on some criteria
    def __init__(self):
        """Executes immediately after program start, on config load"""
        EventSubscriptionController.subscribe_to_multiple_events([
            (RunnerEvents.BEFORE_EXPERIMENT, self.before_experiment),
            (RunnerEvents.BEFORE_RUN       , self.before_run       ),
            (RunnerEvents.START_RUN        , self.start_run        ),
            (RunnerEvents.START_MEASUREMENT, self.start_measurement),
            (RunnerEvents.INTERACT         , self.interact         ),
            (RunnerEvents.STOP_MEASUREMENT , self.stop_measurement ),
            (RunnerEvents.STOP_RUN         , self.stop_run         ),
            (RunnerEvents.POPULATE_RUN_DATA, self.populate_run_data),
            (RunnerEvents.AFTER_EXPERIMENT , self.after_experiment )
        ])
        self.run_table_model = None  # Initialized later
        output.console_log("Custom config loaded")

    def create_run_table_model(self) -> RunTableModel:
        """Create and return the run_table model here. A run_table is a List (rows) of tuples (columns),
        representing each run performed"""
        sampling_factor = FactorModel("sampling_rate", self.sampling_rate_options) # Define different sampling intervals
        input_size_factor = FactorModel("input_size", self.input_size_options)  # Define different input sizes
        cache_factor = FactorModel("cache_strategy", self.target_function_names)  # Different cache strategies
        self.run_table_model = RunTableModel(
            factors=[input_size_factor, sampling_factor, cache_factor],
            data_columns=['input_description','execution_time','average_cpu_usage','memory_usage','energy_consumption', 'dram_energy', 'package_energy', 'pp0_energy', 'pp1_energy']
        )
        return self.run_table_model

    def before_experiment(self) -> None:
        """Perform any activity required before starting the experiment here
        Invoked only once during the lifetime of the program."""
        pass

    def before_run(self) -> None:
        """Perform any activity required before starting a run.
        No context is available here as the run is not yet active (BEFORE RUN)"""
        # packages_dir = os.path.join(self.ROOT_DIR, 'packages')
        pass

    def start_run(self, context: RunnerContext) -> None:
        """Perform any activity required for starting the run here.
        For example, starting the target system to measure.
        Activities after starting the run should also be performed here."""


    def start_measurement(self, context: RunnerContext) -> None:
        """Start energy measurement using Energibridge."""
        sampling_interval = context.run_variation['sampling_rate']
        target_function = context.run_variation['cache_strategy']
        input_size = context.run_variation['input_size']

        # profiler_cmd = f'''sudo energibridge --interval {sampling_interval} \
        # --max-execution 20 \
        # --output {context.run_dir / "energibridge.csv"} \
        # --summary \
        # python3 -c "import sys; import os; import numpy as np; sys.path.append(os.path.join(os.getcwd(), 'packages')); import {target_function_location} as module; X = tuple(np.random.random({input_size})); module.{target_function}(X)"'''

        # separte the command into multiple lines for better readability

        python_cmd = (
            f"import sys; import os; import numpy as np; "
            f"sys.path.append(os.path.join(os.getcwd(), 'packages')); "
            f"import {self.target_function_location} as module; "
            f"X = tuple(np.random.random({input_size})); "
            f"module.{target_function}(X); "
            f"print(f'python_cmd executed successfully')"
        )

        profiler_cmd = (
            f"sudo energibridge --interval {sampling_interval} "
            f"--max-execution 20 "
            f"--output {context.run_dir}/energibridge.csv "
            f"--summary "
            f"python -c \"{python_cmd}\" "
        )

        energibridge_log = open(f'{context.run_dir}/energibridge.log', 'w')
        output.console_log(f"Executing command: {shlex.split(profiler_cmd)}")
        self.profiler = subprocess.Popen(shlex.split(profiler_cmd), stdout=energibridge_log,stderr=energibridge_log)

        energibridge_log.write(f'sampling interval: {sampling_interval}, target function: {target_function}, input size: {input_size}\n')
        energibridge_log.flush()
        energibridge_log.close()

        output.console_log(f"Context.run_nr: {context.run_nr}, sampling interval: {sampling_interval}, target function: {target_function}, input size: {input_size}")
    def interact(self, context: RunnerContext) -> None:
        """Perform any interaction with the running target system here, or block here until the target finishes."""

        # No interaction. We just run it for XX seconds.
        # Another example would be to wait for the target to finish, e.g. via `self.target.wait()`
        output.console_log("Running program for 20 seconds")
        time.sleep(20)


    def stop_measurement(self, context: RunnerContext) -> None:
        """Perform any activity here required for stopping measurements."""
        # self.profiler.kill()
        self.profiler.wait()
        output.console_log("Energy measurement completed.")

    def stop_run(self, context: RunnerContext) -> None:
        """Perform any activity here required for stopping the run.
        Activities after stopping the run should also be performed here."""
        # self.target.kill()
        # self.target.wait()
        pass

    def populate_run_data(self, context: RunnerContext) -> Optional[Dict[str, Any]]:
        """Parse and process any measurement data here.
        You can also store the raw measurement data under `context.run_dir`
        Returns a dictionary with keys `self.run_table_model.data_columns` and their values populated"""
        csv_path = context.run_dir / "energibridge.csv"
        log_path = context.run_dir / "energibridge.log"
        if not csv_path.exists():
            output.console_log(f"Error: File {csv_path} does not exist!")
            return None
        # energibridge.csv - Power consumption of the whole system
        df = pd.read_csv(context.run_dir / "energibridge.csv")
        run_data = {
            'input_description': self.input_description[ math.ceil(context.run_nr/ (len(self.target_function_names) * len(self.sampling_rate_options))) - 1 ],
            'memory_usage': round(df.get('USED_MEMORY', pd.Series([0])).mean()/(1024 ** 2), 8),
            'dram_energy': round(df.get('DRAM_ENERGY (J)', pd.Series([0])).mean(), 8),
            'package_energy': round(df.get('PACKAGE_ENERGY (J)', pd.Series([0])).mean(), 8),
            'pp0_energy': round(df.get('PP0_ENERGY (J)', pd.Series([0])).mean(), 8),
            'pp1_energy': round(df.get('PP1_ENERGY (J)', pd.Series([0])).mean(), 8),
        }

        # Calculate average CPU usage across all cores
        cpu_columns = [col for col in df.columns if col.startswith('CPU_USAGE_')]
        if cpu_columns:
            core_avg_cpu_usage = df[cpu_columns].mean(axis=0)  # Sum up CPU usage of all cores for each row
            overall_avg_cpu_usage = core_avg_cpu_usage.mean()  # Compute the average CPU usage
            run_data['average_cpu_usage'] = round(overall_avg_cpu_usage, 8)

        # Get the execution time (choose one of the two methods)

        # method 1: using time.time() before and after the execution
        # run_data['execution_time'] = getattr(context, 'run_execution_time', None)

        # method 2: Read execution time from the log file
        if log_path.exists():
            try:
                # Implement retry mechanism to handle file read issues
                retries = 5  # Number of retries
                for attempt in range(retries):
                    try:
                        with open(log_path, 'r') as log_file:
                            log_content = log_file.read()
                            # Use regular expression to find the execution time in seconds
                            match = re.search(r"Energy consumption in joules: ([\d\.]+) for ([\d\.]+) sec of execution",log_content)
                            if match:
                                run_data['energy_consumption'] = float(match.group(1))  # Extract energy consumption in joules
                                run_data['execution_time'] = float(match.group(2))  # Extract the execution time in seconds
                            else:
                                output.console_log(f"Warning: No energy consumption or execution time found in {log_path}")
                                time.sleep(1)  # Wait for 1 second before retrying
                    except IOError:
                        output.console_log(f"Error reading file {log_path}. Retrying... ({attempt + 1}/{retries})")
                        time.sleep(1)  # Wait for 1 second before retrying

                if 'execution_time' and 'energy_consumption' not in run_data:
                    output.console_log(f"Error: Unable to retrieve execution time from {log_path} after {retries} attempts.")
            except Exception as e:
                output.console_log(f"Exception occurred while reading log file {log_path}: {e}")
        else:
            output.console_log(f"Error: Log file {log_path} does not exist.")
        return run_data

    def after_experiment(self) -> None:
        """Perform any activity required after stopping the experiment here
        Invoked only once during the lifetime of the program."""
        pass

    # ================================ DO NOT ALTER BELOW THIS LINE ================================
    experiment_path:            Path             = None

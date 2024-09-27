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

class RunnerConfig:
    ROOT_DIR = Path(dirname(realpath(__file__)))

    # ================================ USER SPECIFIC CONFIG ================================
    """The name of the experiment."""
    name:                       str             = "dft_experiment"

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
        self.start_time = None
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
        sampling_factor = FactorModel("sampling", [200, 1000]) # Define different sampling intervals
        input_size_factor = FactorModel("input_size", [1024,4096])  # Define different input sizes
        cache_factor = FactorModel("cache", ["DFT", "DFT_cache", "DFT_lru_cache"])  # Different cache strategies
        self.run_table_model = RunTableModel(
            factors=[input_size_factor, cache_factor, sampling_factor],
            data_columns=['execution_time','average_cpu_usage','dram_energy', 'package_energy', 'pp0_energy', 'pp1_energy']
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
        sampling_interval = context.run_variation['sampling']
        target_function = context.run_variation['cache']
        input_size = context.run_variation['input_size']
        target_function_location = 'cpu.dft'

        self.start_time = time.time()

        profiler_cmd = f'''sudo energibridge --interval {sampling_interval} \
        --max-execution 20 \
        --output {context.run_dir / "energibridge.csv"} \
        --summary \
        python3 -c "import sys; import os; import numpy as np; sys.path.append(os.path.join(os.getcwd(), 'packages')); import {target_function_location} as module; X = tuple(np.random.random({input_size})); module.{target_function}(X)"'''

        energibridge_log = open(f'{context.run_dir}/energibridge.log', 'w')
        self.profiler = subprocess.Popen(shlex.split(profiler_cmd), stdout=energibridge_log)

        end_time = time.time()
        context.run_execution_time = round(end_time - self.start_time, 8)  # Keep the number of seconds of the 8 decimals

        energibridge_log.write(f'sampling interval: {sampling_interval}, target function: {target_function}, input size: {input_size}\n')
        energibridge_log.flush()
        energibridge_log.close()

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
        if not csv_path.exists():
            output.console_log(f"Error: File {csv_path} does not exist!")
            return None

        # energibridge.csv - Power consumption of the whole system
        df = pd.read_csv(context.run_dir / "energibridge.csv")
        run_data = {
            'dram_energy': round(df.get('DRAM_ENERGY (J)', pd.Series([0])).sum(), 3),
            'package_energy': round(df.get('PACKAGE_ENERGY (J)', pd.Series([0])).sum(), 3),
            'pp0_energy': round(df.get('PP0_ENERGY (J)', pd.Series([0])).sum(), 3),
            'pp1_energy': round(df.get('PP1_ENERGY (J)', pd.Series([0])).sum(), 3),
        }

        # Calculate average CPU usage across all cores
        cpu_columns = [col for col in df.columns if col.startswith('CPU_USAGE_')]
        if cpu_columns:
            total_cpu_usage = df[cpu_columns].sum(axis=1)  # Sum up CPU usage of all cores for each row
            average_cpu_usage = total_cpu_usage.mean()  # Compute the average CPU usage
            run_data['average_cpu_usage'] = round(average_cpu_usage, 3)

        # Get the execution time
        run_data['execution_time'] = getattr(context, 'run_execution_time', None)

        return run_data

    def after_experiment(self) -> None:
        """Perform any activity required after stopping the experiment here
        Invoked only once during the lifetime of the program."""
        pass

    # ================================ DO NOT ALTER BELOW THIS LINE ================================
    experiment_path:            Path             = None

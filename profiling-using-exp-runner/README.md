# Structure

1. Original folders and files from ExperimentRunner's git repo include:

- experiment-runner
- test
- test-standalone
- examples(removed by me but you can check at https://github.com/S2-group/experiment-runner)
- requirements.txt
- CITATION.cff
- ExperimentRunnerREADME.md
- LICENSE

2. **Newly created folders or files for our project:**

- **cpu-dft-profiling: profiling cpu-intensive dft problem using ExperimentRunner and EnergiBridge**
- **packages: containing codes for cpu\memory\recursive problems**



## How to run cpu-dft-profiling/RunnerConfig.py in your environment

1. Install Energibridge.

   `Energibridge` is used to measure energy consumption for each run. The energy data is collected and stored in log files and CSV files. To install, please check https://github.com/tdurieux/EnergiBridge. This software can be installed on Linux, MacOS, Windows. 

> **Why Energibridge is used**:
>
> First, it's recommended in lab course.
>
> Secondly, it has an example runner-config.py in the ExperimentRunner's *examples folder* (https://github.com/S2-group/experiment-runner), which allowed me to  modify our own version based on that example. Very convenient!

After installing energibridge, you can run `sudo energibridge --help` in your zsh/bash/shell and if the output is a help documentation, then it means energibridge has already been successfully installed! 

Then, run `sudo chmod+x target/release/energibridge` (this works for me in macos) in your zsh/bash/shell to permit neccessary access to use energibridge.

2. Before running **cpu-dft-profling/RunnerConfig.py**, please remmember to **include *expeirment-runner folder* (consisting ConfigValidator, EventManager, Expe..... in this folder) into the Source Root**, otherwise when you try to run cpu-dft-profling/RunnerConfig.py, it cannot import the following stuff which means cannot run successfully:

> ```python
> from EventManager.Models.RunnerEvents import RunnerEvents
> from EventManager.EventSubscriptionController import EventSubscriptionController
> from ConfigValidator.Config.Models.RunTableModel import RunTableModel
> from ConfigValidator.Config.Models.FactorModel import FactorModel
> from ConfigValidator.Config.Models.RunnerContext import RunnerContext
> from ConfigValidator.Config.Models.OperationType import OperationType
> from ProgressManager.Output.OutputProcedure import OutputProcedure as output
> ```

3. To run  **cpu-dft-profling/RunnerConfig.py**, run following command **at the profiling-using-exp-runner directory **


```python
python experiment-runner/ cpu-dft-profiling/RunnerConfig.py
```

Then it should run smoothly and you can see the ongoing output indicating every run.

### Attention

1. Before running cpu-dft-profilin/RunnerConfig.py, *experiments* folder need to exist in the cpu-dft-profiling folder

2. If you want to re-run the cpu-dft-profilin/RunnerConfig.py, remember to delete or rename dft_experiment folder(which contains all the experiment data you just collected). Otherwise you may not run again and the program will stop because ExperimentRuner is helping you avoid overriding your experiment data.

3. The energy data is collected and stored in log files and CSV files.

4. **For other problems (gd, lemmatization, mergesort, pca, convolve, dijistra, floyd, knapsack, permuatation, fibonacci, hanoi, n_queens, reverse, uniquepaths), just create a new template and modify the template based on this cpu-dft-profilin/RunnerConfig.py.**

5. @cache and @lru_cache need **hashable** input while basic one(the function that doesn't use any cache decorator before definition) doesn't. 

   So when writing corresponding RunnerConfig.py for the remaining problems,  for convenience, modify the input of  basic function to ensure the inputs are same in terms of format(hashable input) among all three functions. (**This modification need to be done with codes located in profiling-using-exp-runner/packages.** At the moment, except for DFT problem, the basic functions for some remaining problem use unhashable inputs. )

## Code Structure

### Factors

- **Sampling Interval**: `200 ms` and `1000 ms`
- **Input Sizes**: `1024`, `4096`
- **Cache Strategies**: `DFT`, `DFT_cache`, `DFT_lru_cache`

So 2x2x3=12 runs. this can be modified. and you will have corresponding different number of runs.

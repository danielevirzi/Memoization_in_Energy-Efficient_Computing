#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Enable extended pattern matching features
shopt -s nullglob

# Function to run profiling for a given directory and type
run_profiling() {
    local dir="$1"
    local type="$2"

    echo "--------------------------------------------"
    echo "Processing directory: $dir"
    echo "Type: $type"
    echo "--------------------------------------------"

    if [[ "$type" == "recursive" ]]; then
        # For recursive type, run the experiment twice
        for run_num in 1 2; do
            echo "Running experiment #$run_num for $dir"

            # Execute the Python command
            python3 experiment-runner/ "$dir"/RunnerConfig.py

            # Define the experiments directory pattern
            # Assuming only one *_experiment directory per run
            experiments_dir=$(find "$dir"/experiments -maxdepth 1 -type d -name "*_experiment" | head -n 1)

            if [[ -d "$experiments_dir" ]]; then
                if [[ "$run_num" -eq 1 ]]; then
                    # Rename after first run
                    new_name="${experiments_dir}_1"
                    mv "$experiments_dir" "$new_name"
                    echo "Renamed $experiments_dir to $new_name"
                elif [[ "$run_num" -eq 2 ]]; then
                    # Rename after second run
                    new_name="${experiments_dir}_2"
                    mv "$experiments_dir" "$new_name"
                    echo "Renamed $experiments_dir to $new_name"
                fi
            else
                echo "Error: *_experiment directory not found in $dir/experiments after run #$run_num."
                exit 1
            fi
        done
    else
        # For cpu and memory types, run the experiment once
        echo "Running experiment for $dir"
        python3 experiment-runner/ "$dir"/RunnerConfig.py

        # Optional: Verify the experiments directory was created
        experiments_dir=$(find "$dir"/experiments -maxdepth 1 -type d -name "*_experiment" | head -n 1)
        if [[ -d "$experiments_dir" ]]; then
            echo "Experiment completed successfully for $dir. Results in $experiments_dir"
        else
            echo "Error: *_experiment directory not found in $dir/experiments after running."
            exit 1
        fi
    fi

    echo "Finished processing $dir"
    echo ""
    echo "sleep for 60 seconds to start the next benchmark"
    sleep 60
}

# Main script execution starts here

# Ensure the script is run from the profiling-using-exp-runner directory
current_dir=$(pwd)
expected_dir="profiling-using-exp-runner"

if [[ "$(basename "$current_dir")" != "$expected_dir" ]]; then
    echo "Error: Please run this script from the '$expected_dir' directory."
    exit 1
fi

echo "Starting profiling experiments in directory: $current_dir"
echo ""

# Iterate over all directories matching profile-<type>-<problem>
for dir in profile-*/; do
    # Remove trailing slash
    dir="${dir%/}"

    # Extract the type by splitting the directory name
    IFS='-' read -r prefix type problem <<< "$dir"

    # Validate the type
    if [[ "$type" != "recursive" && "$type" != "cpu" && "$type" != "memory" ]]; then
        echo "Skipping directory '$dir': Unknown type '$type'"
        echo ""
        continue
    fi

    # Run profiling for the directory
    run_profiling "$dir" "$type"
done

echo "All profiling experiments have been completed successfully."

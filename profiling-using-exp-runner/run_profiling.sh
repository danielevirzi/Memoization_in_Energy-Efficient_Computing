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

    # Define the experiments directory path
    experiments_dir="$dir/experiments"

    # Check if the experiments directory exists
    if [[ -d "$experiments_dir" ]]; then
        echo "Experiments directory exists. Deleting its contents..."
        # Delete all contents within the experiments directory
        rm -rf "$experiments_dir"/*
    else
        echo "Experiments directory does not exist. Creating it..."
        # Create the experiments directory
        mkdir -p "$experiments_dir"
    fi

    # Execute the Python command
    python3 experiment-runner/ "$dir"/RunnerConfig.py

    # Optional: Verify the experiments directory was created or updated
    if [[ -d "$experiments_dir" ]]; then
        echo "Experiment completed successfully for $dir. Results in $experiments_dir"
    else
        echo "Error: experiments directory not found in $dir after running."
        exit 1
    fi

    echo "Finished processing $dir"
    echo ""
    echo "Sleeping for 60 seconds before starting the next benchmark..."
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

# Define the types to look for
TYPES=("cpu" "memory" "recursive")

# Iterate over all directories matching profile-<type>-<problem>
for type in "${TYPES[@]}"; do
    for dir in profile-"$type"-*/; do
        # Remove trailing slash
        dir="${dir%/}"

        # Extract the problem part by removing the prefix
        problem="${dir#profile-$type-}"

        echo "Found directory: $dir with type: $type and problem: $problem"

        # Run profiling for the directory
        run_profiling "$dir" "$type"
    done
done

echo "All profiling experiments have been completed successfully."

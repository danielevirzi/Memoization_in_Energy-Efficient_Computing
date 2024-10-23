#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Define the types to look for
TYPES=("recursive" "cpu" "memory")

# Define the source and destination directories
SOURCE_PARENT_DIR=$(pwd)
DEST_DIR="$SOURCE_PARENT_DIR/FINAL_RESULTS"

# Create the destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

echo "Starting to move experiments to FINAL_RESULTS..."

# Iterate over each type
for type in "${TYPES[@]}"; do
    # Find directories matching the pattern profile-<type>-<problem>
    for dir in "$SOURCE_PARENT_DIR"/profile-"$type"-*; do
        # Check if the directory exists and is indeed a directory
        if [[ -d "$dir" ]]; then
            echo "Processing directory: $dir"

            # Define the experiments directory
            EXPERIMENTS_DIR="$dir/experiments"

            # Check if the experiments directory exists
            if [[ -d "$EXPERIMENTS_DIR" ]]; then
                # Move all contents from experiments directory to FINAL_RESULTS
                echo "Moving contents from $EXPERIMENTS_DIR to $DEST_DIR"
                mv "$EXPERIMENTS_DIR"/* "$DEST_DIR"/

                echo "Successfully moved contents from $EXPERIMENTS_DIR to $DEST_DIR"
            else
                echo "No experiments directory found in $dir. Skipping..."
            fi
        else
            echo "No directory found matching pattern profile-$type-*. Skipping..."
        fi
    done
done

echo "All experiments have been moved to FINAL_RESULTS."

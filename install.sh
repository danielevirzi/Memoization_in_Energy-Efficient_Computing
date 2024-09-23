#!/bin/bash

#Generated with Ai for explorative 

# Function to install dependencies
install_dependencies() {
    pip install -r requirements.txt
    python -m spacy download en_core_web_sm
}

# Check the operating system
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Detected macOS"
    install_dependencies
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Detected Linux"
    install_dependencies
else
    echo "Unsupported OS: $OSTYPE"
    exit 1
fi

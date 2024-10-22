# before creating the image you are supposed to 
#have already cloned energiebridge and experiment runner repos 
#! this should not be used to collect real data, only to test if stuff is working

#partially written with AI for explorative purposes

FROM ubuntu:latest

# Avoid prompts
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python3 python3-pip curl && \
    apt-get install -y iputils-ping nano python3.12-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /stuff

# Copy any necessary files (if needed)
COPY requirements.txt .

# Create a virtual environment
RUN python3 -m venv venv

RUN ./venv/bin/pip install --upgrade pip

# Install the Python dependencies
RUN ./venv/bin/pip install --no-cache-dir -r requirements.txt

# Install Rust and Cargo using rustup
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y

# Set environment variables for Rust
ENV PATH="/root/.cargo/bin:${PATH}"

# Set up the EnergiBridge directory (assumes it's in your context)
COPY EnergiBridge /stuff/EnergiBridge

# Build the EnergiBridge project
WORKDIR /stuff/EnergiBridge
RUN cargo build --release

# Change permissions and copy the built binary to the desired location
RUN chmod +x target/release/energibridge && \
    cp target/release/energibridge /usr/local/bin/


# Set up the experiment-runner directory (assumes it's in your context)
COPY experiment-runner /stuff/experiment-runner

# Install requirements from experiment-runner
WORKDIR /stuff/experiment-runner
RUN ./venv/bin/pip install --no-cache-dir -r requirements.txt

# Set up SSH
#RUN mkdir /var/run/sshd
#RUN echo 'root:icecream03' | chpasswd  
#RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Expose SSH port
#EXPOSE 22

# At container start
CMD ["/bin/bash"]

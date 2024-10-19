# README

# Introduction

This project aims to evaluate and analyze the performance of functions categorized into three distinct types: **CPU-intensive**, **Memory-intensive**, and **Recursive**. 

Each category encompasses five unique problem.

## Function Categories

### 1. CPU-Intensive Functions

These functions primarily demand significant CPU resources

- **DFT** (Discrete Fourier Transform)
- **Hessian**
- **Lemmatization**
- **MergeSort**
- **PCA** (Principal Component Analysis)

### 2. Memory-Intensive Functions

Memory-intensive functions require substantial memory allocation and management

- **Convolve**
- **Dijkstra**
- **Floyd**
- **Knapsack**
- **Permutation**

### 3. Recursive Functions

Recursive functions utilize self-referential logic

- **Fibonacci**
- **Hanoi**
- **N_Queens**
- **Reverse**
- **UniquePaths**

## Directory Structure

To profile each problem, each problem's profiling codes are organized into its own directory following a consistent naming convention: `profile-<type>-<problem>`. For example:

- `profile-cpu-dft`
- `profile-memory-convolve`
- `profile-recursive-fibonacci`

## Experimental Environment Setup

Setting up the experimental environment involves configuring a Raspberry Pi with Ubuntu Server and preparing it for remote operations. Follow the steps below to set up your environment.

### 1. Flashing the Raspberry Pi

**Materials Needed:**

- Raspberry Pi
- SD card
- SD card reader
- Laptop

**Steps:**

1. Prepare the SD Card:
   - Remove the SD card from the Raspberry Pi and insert it into the SD card reader connected to laptop.
2. Download and Install Raspberry Pi Imager:
3. Configure the Custom OS:
   - Open the Raspberry Pi Imager application.
   - Choose **Ubuntu Server 20.04.5 LTS (64-bit)** as the operating system.
   - Select the SD card from the storage list.
4. Set Up Advanced Configuration:
   - configure the following:
     - **Hostname:** `raspberrypi.local`
     - **Username:** `greenlab`
     - **Password:** `greenlab`
     - WiFi Configuration:
       - **SSID:** *Your WiFi Network Name*
       - **Password:** *Your WiFi Password*
       - **Country:** `NL` (Netherlands)
     - **Timezone:** `Europe/Amsterdam`
     - **Keyboard Layout:** `US`
     - **Enable SSH:** Yes (**Allow SSH access with password login**)
5. Flash the OS:
   - After configuring, proceed to write the OS to the SD card. This process will erase all existing data on the card.

### 2. Configuring WiFi on Ubuntu Server

We utilized Raspberry Pi's official tools and the officially provided Ubuntu Server image, following the standard configuration methods. 

**However, here has an issue where the system failed to connect to the WiFi network automatically upon startup.**

**Solution:** To resolve this, we manually edited the `network-config` file to include `hidden: true`. 

**Steps:**

1. Reinsert the SD Card:
   - Once flashing is complete, remove the SD card from the Raspberry Pi and reinsert it into the SD card reader connected to your computer.
2. Edit the `network-config` File:
   - Locate the `network-config` file on the SD card.
   - Open it with vscode editor and modify it as shown below. 

```yaml
wifis:
  wlan0:
    dhcp4: true
    optional: true
    access-points:
      "Your_WIFI_NAME":
        **hidden: true
        password: "Your_Wifi_Password"
```

3. Safely eject the SD Card:
   - Ensure all changes are saved, then safely eject the SD card from your computer.

### 3. Setting Up the Raspberry Pi Environment

**Steps:**

1. Insert the SD Card:
   - Place the configured SD card back into the Raspberry Pi.
2. Power Up:
   - Connect the Raspberry Pi to your computer and power it on. Wait for a minute or two to allow it to connect to the WiFi network.
3. Find the Raspberry Pi's IP Address:
   - You can access your router's management page to locate the Raspberry Pi's IP address
4. **SSH into the Raspberry Pi:**
   - Open a terminal on your laptop and connect to the Raspberry Pi using SSH

```bash
ssh greenlab@<Raspberry_Pi_IP_Address>
```

Enter the password `greenlab` 

5. Once logged in, update the package lists and upgrade the system packages

```bash
sudo apt update
sudo apt upgrade -y
```

6. Install pip3

```bash
sudo apt install python3-pip -y
```

### 4. Configure Github SSH

**Steps:**

1. Generate SSH Key:

   - Generate a new SSH key pair **without a passphrase:**

   **Important:** Do **not** set a passphrase. This is crucial for the proper functioning of `energibridge` during experiments, as a passphrase would interfere with the automated processes required.

2. Add SSH Key to GitHub

### 5. Clone the Repository

```bash
mkdir ~/greenlab
cd ~/greenlab
git clone git@github.com:Quartinocci/greenlab_vu.git
```

### 6. Install Required Python Packages:

Experiment Runner needs following:

```bash
pip3 install pandas psutil tabulate dill jsonpickle
```

### 7. Configuring Remote Laptop for SSH Access

To allow the Raspberry Pi to remotely access your laptop via SSH, follow these steps:

**Steps:**

1. **Ensure SSH Key Exists on Raspberry Pi:**

The SSH key was generated in the configure Github SSH steps. If not, generate one.

2. **Copy SSH Key to Laptop:**

- Use `ssh-copy-id` to copy the Raspberry Pi's public key to your laptop

```bash
ssh-copy-id <your_laptop_username>@<Laptop_IP_Address>
```

Replace `<Laptop_IP_Address>` with your laptop's actual IP address, which can be found using:`ifconfig`

3. **Enable Remote Login on Laptop:**

- On your laptop, ensure that remote login via SSH is enabled. 

4. **Test SSH Connection from Raspberry Pi to Laptop**

From the Raspberry Pi terminal, attempt to SSH into your laptop.

## Running the code

To execute the profiling experiments, follow the steps below:

### 1. Modify SSH-Related Information in `RunnerConfig.py`

Before running the profiling code, you need to update the SSH configuration details to match your environment.

**Steps to Modify:**

1. **Navigate to the Problem Directory:** for example, profile-cpu-dft directory

2. **Edit the RunnerConfig.py**:

   Update the following variables:

- **`name`**: Set the name of the experiment (e.g., `"dft_experiment"`).
- **`target_function_location`**: Specify the module path of the target function in the remote laptop (e.g., `'cpu.dft'`).
- **`target_function_names`**: List the different variations of the target function you intend to profile (e.g., `["DFT", "DFT_cache", "DFT_lru_cache"]`).
- **`input_size_options`**: Define the different input sizes to be used in the experiments (e.g., `[1024, 4096, 8192]`).
- **`input_description`**: Provide descriptions corresponding to each input size for clarity in results (e.g., `["1024 points", "4096 points", "8192 points"]`).
- **`sampling_rate_options`**: Set the sampling rates for profiling (e.g., `[200]`).
- **`time_between_runs_in_ms`**: Configure the cooldown period between runs in milliseconds (e.g., `60000` for 1 minute).
- **`results_output_path`**: Define the path where the results will be stored (e.g., `Path(dirname(realpath(__file__))) / 'experiments'`).
- **`operation_type`**: Choose the operation type, typically `OperationType.AUTO` for automated runs.
- **`remote_user`**: Set the SSH username for the remote laptop (e.g., `"rr"`).
- **`remote_host`**: Specify the IP address of the remote laptop (e.g., `"192.168.0.105"`).
- **`remote_package_dir`**: Provide the path to the packages directory on the remote laptop (e.g., `"/Users/rr/GreenLab/ProjectCode/profiling-using-exp-runner/packages"`).
- **`remote_temporary_results_dir`**: Define the path where temporary results will be stored on the remote laptop (e.g., `"/Users/rr/GreenLab/ProjectCode/profiling-using-exp-runner/RESULTS"`).
- **`energibridge_location`**: Specify the path to the `energibridge` executable on the remote laptop (e.g., `"/usr/local/bin/energibridge"`).

```python
class RunnerConfig:
    ROOT_DIR = Path(dirname(realpath(__file__)))

    # ================================ USER SPECIFIC CONFIG ================================
    """The name of the experiment."""
    name:                       str             = "dft_experiment"
    """target function location in remote laptop"""
    target_function_location = 'cpu.dft'
    target_function_names = ["DFT", "DFT_cache", "DFT_lru_cache"]
    input_size_options = [1024, 4096, 8192]
    input_description = ["1024 points", "4096 points", "8192 points"]
    sampling_rate_options = [200]
    """The time Experiment Runner will wait after a run completes.
    This can be essential to accommodate for cooldown periods on some systems."""
    time_between_runs_in_ms:    int             = 60000

    """The path in which Experiment Runner will create a folder with the name `self.name`, in order to store the
    results from this experiment. (Path does not need to exist - it will be created if necessary.)
    Output path defaults to the config file's path, inside the folder 'experiments'"""
    results_output_path:        Path             = ROOT_DIR / 'experiments'

    """Experiment operation type. Unless you manually want to initiate each run, use `OperationType.AUTO`."""
    operation_type:             OperationType   = OperationType.AUTO

    """remote ssh connection details"""
    remote_user:                str             = "rr"
    remote_host:                str             = "192.168.0.105"

    """remote path to the experiment"""
    remote_package_dir:        str             = "/Users/rr/GreenLab/ProjectCode/profiling-using-exp-runner/packages"
    remote_temporary_results_dir:        str             = "/Users/rr/GreenLab/ProjectCode/profiling-using-exp-runner/RESULTS"

    """energibridge location in remote laptop"""
    energibridge_location:        str             = "/usr/local/bin/energibridge"
```

### 2. Run the profiling code

**Steps:**

1. **Navigate to the `profiling-using-exp-runner` Directory**
2. Run following command:

```python
python experiment-runner/ profile-<type>-<problem>/RunnerConfig.py
```


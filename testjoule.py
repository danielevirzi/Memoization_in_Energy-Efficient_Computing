from pyJoules.device.rapl_device import RaplPackageDomain
from pyJoules.energy_meter import measure_energy

# Define the function you want to monitor
@measure_energy(domains=[RaplPackageDomain(0)])
def my_function():
    # Your code here
    for i in range(10000000):
        pass

# Call the function
my_function()

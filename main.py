# Importing the packages
from packages.cpu import *
from packages.memory import *
from packages.recursive import *

"""
from pyJoules.energy_meter import measure_energy
@measure_energy
def foo():
	# Instructions to be evaluated.

foo()
"""

print(cpu.is_prime(29)) 

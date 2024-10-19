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
import re
import math


def dict_to_frozenset(d: dict) -> frozenset:
    return frozenset((k, frozenset(v.items())) for k, v in d.items())

class RunnerConfig:
    ROOT_DIR = Path(dirname(realpath(__file__)))

    # ================================ USER SPECIFIC CONFIG ================================
    """The name of the experiment."""
    name:                       str             = "fibonacci_experiment"
    """target function location in remote laptop"""
    target_function_location = 'memory.dijkstra'
    target_function_names = ['dijkstra', 'dijkstra_cache', 'fibonacci_lru_cache']
    graph_15 = {
        'A': {'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 1, 'G': 6, 'H': 2, 'I': 7, 'J': 3, 'K': 4, 'L': 5, 'M': 6, 'N': 7,
              'O': 8},
        'B': {'A': 2, 'C': 6, 'D': 7, 'E': 3, 'F': 8, 'G': 4, 'H': 5, 'I': 1, 'J': 9, 'K': 2, 'L': 3, 'M': 4, 'N': 5,
              'O': 6},
        'C': {'A': 3, 'B': 6, 'D': 2, 'E': 8, 'F': 7, 'G': 3, 'H': 4, 'I': 9, 'J': 5, 'K': 6, 'L': 7, 'M': 8, 'N': 9,
              'O': 1},
        'D': {'A': 4, 'B': 7, 'C': 2, 'E': 6, 'F': 5, 'G': 1, 'H': 8, 'I': 2, 'J': 7, 'K': 3, 'L': 4, 'M': 5, 'N': 6,
              'O': 7},
        'E': {'A': 5, 'B': 3, 'C': 8, 'D': 6, 'F': 4, 'G': 7, 'H': 2, 'I': 5, 'J': 6, 'K': 1, 'L': 2, 'M': 3, 'N': 4,
              'O': 5},
        'F': {'A': 1, 'B': 8, 'C': 7, 'D': 5, 'E': 4, 'G': 2, 'H': 3, 'I': 6, 'J': 4, 'K': 5, 'L': 6, 'M': 7, 'N': 8,
              'O': 9},
        'G': {'A': 6, 'B': 4, 'C': 3, 'D': 1, 'E': 7, 'F': 2, 'H': 5, 'I': 3, 'J': 8, 'K': 9, 'L': 1, 'M': 2, 'N': 3,
              'O': 4},
        'H': {'A': 2, 'B': 5, 'C': 4, 'D': 8, 'E': 2, 'F': 3, 'G': 5, 'I': 1, 'J': 7, 'K': 8, 'L': 2, 'M': 3, 'N': 4,
              'O': 5},
        'I': {'A': 7, 'B': 1, 'C': 9, 'D': 2, 'E': 5, 'F': 6, 'G': 3, 'H': 1, 'J': 2, 'K': 3, 'L': 4, 'M': 5, 'N': 6,
              'O': 7},
        'J': {'A': 3, 'B': 9, 'C': 5, 'D': 7, 'E': 6, 'F': 4, 'G': 8, 'H': 7, 'I': 2, 'K': 1, 'L': 2, 'M': 3, 'N': 4,
              'O': 5},
        'K': {'A': 4, 'B': 2, 'C': 6, 'D': 3, 'E': 1, 'F': 5, 'G': 9, 'H': 8, 'I': 3, 'J': 1, 'L': 6, 'M': 7, 'N': 8,
              'O': 9},
        'L': {'A': 5, 'B': 3, 'C': 7, 'D': 4, 'E': 2, 'F': 6, 'G': 1, 'H': 2, 'I': 4, 'J': 2, 'K': 6, 'M': 8, 'N': 9,
              'O': 1},
        'M': {'A': 6, 'B': 4, 'C': 8, 'D': 5, 'E': 3, 'F': 7, 'G': 2, 'H': 3, 'I': 5, 'J': 3, 'K': 7, 'L': 8, 'N': 1,
              'O': 2},
        'N': {'A': 7, 'B': 5, 'C': 9, 'D': 6, 'E': 4, 'F': 8, 'G': 3, 'H': 4, 'I': 6, 'J': 4, 'K': 8, 'L': 9, 'M': 1,
              'O': 3},
        'O': {'A': 8, 'B': 6, 'C': 1, 'D': 7, 'E': 5, 'F': 9, 'G': 4, 'H': 5, 'I': 7, 'J': 5, 'K': 9, 'L': 1, 'M': 2,
              'N': 3}
    }
    graph_20 = {
        'A': {'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 1, 'G': 6, 'H': 2, 'I': 7, 'J': 3, 'K': 5, 'L': 4, 'M': 2, 'N': 6,
              'O': 3, 'P': 7, 'Q': 4, 'R': 8, 'S': 2, 'T': 9},
        'B': {'A': 2, 'C': 6, 'D': 7, 'E': 3, 'F': 8, 'G': 4, 'H': 5, 'I': 1, 'J': 9, 'K': 2, 'L': 3, 'M': 7, 'N': 6,
              'O': 4, 'P': 8, 'Q': 5, 'R': 1, 'S': 2, 'T': 6},
        'C': {'A': 3, 'B': 6, 'D': 2, 'E': 8, 'F': 7, 'G': 3, 'H': 4, 'I': 9, 'J': 5, 'K': 6, 'L': 4, 'M': 7, 'N': 8,
              'O': 9, 'P': 1, 'Q': 2, 'R': 3, 'S': 4, 'T': 7},
        'D': {'A': 4, 'B': 7, 'C': 2, 'E': 6, 'F': 5, 'G': 1, 'H': 8, 'I': 2, 'J': 7, 'K': 3, 'L': 5, 'M': 6, 'N': 9,
              'O': 2, 'P': 4, 'Q': 8, 'R': 6, 'S': 7, 'T': 1},
        'E': {'A': 5, 'B': 3, 'C': 8, 'D': 6, 'F': 4, 'G': 7, 'H': 2, 'I': 5, 'J': 6, 'K': 1, 'L': 4, 'M': 8, 'N': 3,
              'O': 7, 'P': 9, 'Q': 5, 'R': 3, 'S': 6, 'T': 2},
        'F': {'A': 1, 'B': 8, 'C': 7, 'D': 5, 'E': 4, 'G': 2, 'H': 3, 'I': 6, 'J': 4, 'K': 2, 'L': 5, 'M': 7, 'N': 8,
              'O': 6, 'P': 3, 'Q': 9, 'R': 5, 'S': 1, 'T': 4},
        'G': {'A': 6, 'B': 4, 'C': 3, 'D': 1, 'E': 7, 'F': 2, 'H': 5, 'I': 3, 'J': 8, 'K': 9, 'L': 1, 'M': 4, 'N': 6,
              'O': 7, 'P': 2, 'Q': 5, 'R': 3, 'S': 9, 'T': 8},
        'H': {'A': 2, 'B': 5, 'C': 4, 'D': 8, 'E': 2, 'F': 3, 'G': 5, 'I': 1, 'J': 7, 'K': 8, 'L': 2, 'M': 6, 'N': 7,
              'O': 9, 'P': 5, 'Q': 4, 'R': 3, 'S': 2, 'T': 1},
        'I': {'A': 7, 'B': 1, 'C': 9, 'D': 2, 'E': 5, 'F': 6, 'G': 3, 'H': 1, 'J': 2, 'K': 3, 'L': 9, 'M': 5, 'N': 2,
              'O': 4, 'P': 8, 'Q': 1, 'R': 7, 'S': 6, 'T': 5},
        'J': {'A': 3, 'B': 9, 'C': 5, 'D': 7, 'E': 6, 'F': 4, 'G': 8, 'H': 7, 'I': 2, 'K': 1, 'L': 2, 'M': 4, 'N': 5,
              'O': 9, 'P': 6, 'Q': 3, 'R': 5, 'S': 4, 'T': 6},
        'K': {'A': 5, 'B': 2, 'C': 6, 'D': 3, 'E': 1, 'F': 5, 'G': 9, 'H': 8, 'I': 3, 'J': 1, 'L': 6, 'M': 7, 'N': 8,
              'O': 9, 'P': 2, 'Q': 4, 'R': 3, 'S': 5, 'T': 7},
        'L': {'A': 4, 'B': 3, 'C': 4, 'D': 5, 'E': 4, 'F': 6, 'G': 1, 'H': 2, 'I': 9, 'J': 2, 'K': 6, 'M': 7, 'N': 8,
              'O': 9, 'P': 1, 'Q': 5, 'R': 2, 'S': 8, 'T': 3},
        'M': {'A': 2, 'B': 7, 'C': 7, 'D': 6, 'E': 8, 'F': 7, 'G': 4, 'H': 6, 'I': 5, 'J': 4, 'K': 7, 'L': 7, 'N': 6,
              'O': 3, 'P': 8, 'Q': 9, 'R': 5, 'S': 4, 'T': 2},
        'N': {'A': 6, 'B': 6, 'C': 8, 'D': 9, 'E': 3, 'F': 8, 'G': 6, 'H': 7, 'I': 2, 'J': 5, 'K': 8, 'L': 8, 'M': 6,
              'O': 4, 'P': 9, 'Q': 1, 'R': 2, 'S': 7, 'T': 5},
        'O': {'A': 3, 'B': 4, 'C': 9, 'D': 2, 'E': 7, 'F': 6, 'G': 7, 'H': 9, 'I': 4, 'J': 9, 'K': 9, 'L': 9, 'M': 3,
              'N': 4, 'P': 2, 'Q': 6, 'R': 7, 'S': 8, 'T': 9},
        'P': {'A': 7, 'B': 8, 'C': 1, 'D': 4, 'E': 9, 'F': 3, 'G': 2, 'H': 5, 'I': 8, 'J': 6, 'K': 2, 'L': 1, 'M': 8,
              'N': 9, 'O': 2, 'Q': 6, 'R': 4, 'S': 3, 'T': 9},
        'Q': {'A': 4, 'B': 5, 'C': 2, 'D': 8, 'E': 5, 'F': 9, 'G': 5, 'H': 4, 'I': 1, 'J': 3, 'K': 4, 'L': 5, 'M': 9,
              'N': 1, 'O': 6, 'P': 6, 'R': 3, 'S': 9, 'T': 5},
        'R': {'A': 8, 'B': 1, 'C': 3, 'D': 6, 'E': 3, 'F': 5, 'G': 3, 'H': 3, 'I': 7, 'J': 5, 'K': 3, 'L': 2, 'M': 5,
              'N': 2, 'O': 7, 'P': 4, 'Q': 3, 'S': 1, 'T': 9},
        'S': {'A': 2, 'B': 2, 'C': 4, 'D': 7, 'E': 6, 'F': 1, 'G': 9, 'H': 2, 'I': 6, 'J': 4, 'K': 5, 'L': 8, 'M': 4,
              'N': 7, 'O': 8, 'P': 3, 'Q': 9, 'R': 1, 'T': 5},
        'T': {'A': 9, 'B': 6, 'C': 7, 'D': 1, 'E': 2, 'F': 4, 'G': 8, 'H': 1, 'I': 5, 'J': 6, 'K': 7, 'L': 3, 'M': 2,
              'N': 5, 'O': 9, 'P': 9, 'Q': 5, 'R': 9, 'S': 5}
    }
    graph_25 = {
        'A': {'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 1, 'G': 6, 'H': 2, 'I': 7, 'J': 3, 'K': 5, 'L': 4, 'M': 2, 'N': 6,
              'O': 3, 'P': 7, 'Q': 4, 'R': 8, 'S': 2, 'T': 9, 'U': 4, 'V': 5, 'W': 7, 'X': 3, 'Y': 6},
        'B': {'A': 2, 'C': 6, 'D': 7, 'E': 3, 'F': 8, 'G': 4, 'H': 5, 'I': 1, 'J': 9, 'K': 2, 'L': 3, 'M': 7, 'N': 6,
              'O': 4, 'P': 8, 'Q': 5, 'R': 1, 'S': 2, 'T': 6, 'U': 7, 'V': 3, 'W': 4, 'X': 9, 'Y': 5},
        'C': {'A': 3, 'B': 6, 'D': 2, 'E': 8, 'F': 7, 'G': 3, 'H': 4, 'I': 9, 'J': 5, 'K': 6, 'L': 4, 'M': 7, 'N': 8,
              'O': 9, 'P': 1, 'Q': 2, 'R': 3, 'S': 4, 'T': 7, 'U': 8, 'V': 1, 'W': 5, 'X': 4, 'Y': 2},
        'D': {'A': 4, 'B': 7, 'C': 2, 'E': 6, 'F': 5, 'G': 1, 'H': 8, 'I': 2, 'J': 7, 'K': 3, 'L': 5, 'M': 6, 'N': 9,
              'O': 2, 'P': 4, 'Q': 8, 'R': 6, 'S': 7, 'T': 1, 'U': 5, 'V': 6, 'W': 3, 'X': 2, 'Y': 7},
        'E': {'A': 5, 'B': 3, 'C': 8, 'D': 6, 'F': 4, 'G': 7, 'H': 2, 'I': 5, 'J': 6, 'K': 1, 'L': 4, 'M': 8, 'N': 3,
              'O': 7, 'P': 9, 'Q': 5, 'R': 3, 'S': 6, 'T': 2, 'U': 8, 'V': 9, 'W': 7, 'X': 4, 'Y': 1},
        'F': {'A': 1, 'B': 8, 'C': 7, 'D': 5, 'E': 4, 'G': 2, 'H': 3, 'I': 6, 'J': 4, 'K': 2, 'L': 5, 'M': 7, 'N': 8,
              'O': 6, 'P': 3, 'Q': 9, 'R': 5, 'S': 1, 'T': 4, 'U': 6, 'V': 7, 'W': 9, 'X': 1, 'Y': 8},
        'G': {'A': 6, 'B': 4, 'C': 3, 'D': 1, 'E': 7, 'F': 2, 'H': 5, 'I': 3, 'J': 8, 'K': 9, 'L': 1, 'M': 4, 'N': 6,
              'O': 7, 'P': 2, 'Q': 5, 'R': 3, 'S': 9, 'T': 8, 'U': 7, 'V': 2, 'W': 4, 'X': 5, 'Y': 3},
        'H': {'A': 2, 'B': 5, 'C': 4, 'D': 8, 'E': 2, 'F': 3, 'G': 5, 'I': 1, 'J': 7, 'K': 8, 'L': 2, 'M': 6, 'N': 7,
              'O': 9, 'P': 5, 'Q': 4, 'R': 3, 'S': 2, 'T': 1, 'U': 4, 'V': 6, 'W': 9, 'X': 8, 'Y': 7},
        'I': {'A': 7, 'B': 1, 'C': 9, 'D': 2, 'E': 5, 'F': 6, 'G': 3, 'H': 1, 'J': 2, 'K': 3, 'L': 9, 'M': 5, 'N': 2,
              'O': 4, 'P': 8, 'Q': 1, 'R': 7, 'S': 6, 'T': 5, 'U': 3, 'V': 9, 'W': 4, 'X': 2, 'Y': 8},
        'J': {'A': 3, 'B': 9, 'C': 5, 'D': 7, 'E': 6, 'F': 4, 'G': 8, 'H': 7, 'I': 2, 'K': 1, 'L': 2, 'M': 4, 'N': 5,
              'O': 9, 'P': 6, 'Q': 3, 'R': 5, 'S': 4, 'T': 6, 'U': 1, 'V': 8, 'W': 3, 'X': 5, 'Y': 2},
        'K': {'A': 5, 'B': 2, 'C': 6, 'D': 3, 'E': 1, 'F': 5, 'G': 9, 'H': 8, 'I': 3, 'J': 1, 'L': 6, 'M': 7, 'N': 8,
              'O': 9, 'P': 2, 'Q': 4, 'R': 3, 'S': 5, 'T': 7, 'U': 4, 'V': 3, 'W': 9, 'X': 8, 'Y': 7},
        'L': {'A': 4, 'B': 3, 'C': 4, 'D': 5, 'E': 4, 'F': 6, 'G': 1, 'H': 2, 'I': 9, 'J': 2, 'K': 6, 'M': 7, 'N': 8,
              'O': 9, 'P': 1, 'Q': 5, 'R': 2, 'S': 8, 'T': 3, 'U': 9, 'V': 2, 'W': 5, 'X': 4, 'Y': 1},
        'M': {'A': 2, 'B': 7, 'C': 7, 'D': 6, 'E': 8, 'F': 7, 'G': 4, 'H': 6, 'I': 5, 'J': 4, 'K': 7, 'L': 7, 'N': 6,
              'O': 3, 'P': 8, 'Q': 9, 'R': 5, 'S': 4, 'T': 2, 'U': 1, 'V': 3, 'W': 7, 'X': 5, 'Y': 6},
        'N': {'A': 6, 'B': 6, 'C': 8, 'D': 9, 'E': 3, 'F': 8, 'G': 6, 'H': 7, 'I': 2, 'J': 5, 'K': 8, 'L': 8, 'M': 6,
              'O': 4, 'P': 9, 'Q': 2, 'R': 1, 'S': 5, 'T': 6, 'U': 2, 'V': 7, 'W': 8, 'X': 9, 'Y': 3},
        'O': {'A': 3, 'B': 4, 'C': 9, 'D': 2, 'E': 7, 'F': 6, 'G': 8, 'H': 9, 'I': 4, 'J': 1, 'K': 9, 'L': 9, 'M': 3,
              'N': 4, 'P': 2, 'Q': 3, 'R': 4, 'S': 5, 'T': 9, 'U': 7, 'V': 1, 'W': 2, 'X': 4, 'Y': 5},
        'P': {'A': 7, 'B': 8, 'C': 9, 'D': 4, 'E': 9, 'F': 3, 'G': 2, 'H': 5, 'I': 8, 'J': 6, 'K': 2, 'L': 1, 'M': 8,
              'N': 9, 'O': 2, 'Q': 5, 'R': 7, 'S': 8, 'T': 4, 'U': 3, 'V': 2, 'W': 1, 'X': 9, 'Y': 7},
        'Q': {'A': 4, 'B': 3, 'C': 7, 'D': 8, 'E': 6, 'F': 9, 'G': 5, 'H': 4, 'I': 1, 'J': 3, 'K': 4, 'L': 5, 'M': 9,
              'N': 2, 'O': 3, 'P': 5, 'R': 9, 'S': 9, 'T': 3, 'U': 1, 'V': 7, 'W': 6, 'X': 8, 'Y': 4},
        'R': {'A': 8, 'B': 1, 'C': 3, 'D': 6, 'E': 3, 'F': 5, 'G': 3, 'H': 3, 'I': 7, 'J': 5, 'K': 3, 'L': 2, 'M': 5,
              'N': 2, 'O': 7, 'P': 4, 'Q': 3, 'S': 1, 'T': 9, 'U': 4, 'V': 5, 'W': 7, 'X': 3, 'Y': 6},
        'S': {'A': 2, 'B': 2, 'C': 4, 'D': 7, 'E': 6, 'F': 1, 'G': 9, 'H': 2, 'I': 6, 'J': 4, 'K': 5, 'L': 8, 'M': 4,
              'N': 7, 'O': 8, 'P': 3, 'Q': 9, 'R': 1, 'T': 5, 'U': 7, 'V': 2, 'W': 3, 'X': 6, 'Y': 9},
        'T': {'A': 9, 'B': 6, 'C': 7, 'D': 1, 'E': 2, 'F': 4, 'G': 8, 'H': 1, 'I': 5, 'J': 6, 'K': 7, 'L': 3, 'M': 2,
              'N': 5, 'O': 9, 'P': 9, 'Q': 5, 'R': 9, 'S': 5, 'U': 8, 'V': 4, 'W': 2, 'X': 7, 'Y': 3},
        'U': {'A': 4, 'B': 7, 'C': 8, 'D': 5, 'E': 9, 'F': 6, 'G': 7, 'H': 8, 'I': 3, 'J': 4, 'K': 7, 'L': 9, 'M': 1,
              'N': 6, 'O': 4, 'P': 3, 'Q': 1, 'R': 4, 'S': 7, 'T': 8, 'V': 2, 'W': 9, 'X': 5, 'Y': 6},
        'V': {'A': 5, 'B': 9, 'C': 1, 'D': 3, 'E': 9, 'F': 7, 'G': 4, 'H': 3, 'I': 8, 'J': 3, 'K': 9, 'L': 8, 'M': 2,
              'N': 7, 'O': 3, 'P': 2, 'Q': 7, 'R': 5, 'S': 2, 'T': 4, 'U': 9, 'W': 1, 'X': 6, 'Y': 4},
        'W': {'A': 7, 'B': 4, 'C': 5, 'D': 6, 'E': 7, 'F': 9, 'G': 4, 'H': 9, 'I': 6, 'J': 5, 'K': 4, 'L': 5, 'M': 7,
              'N': 8, 'O': 2, 'P': 1, 'Q': 6, 'R': 7, 'S': 3, 'T': 2, 'U': 9, 'V': 1, 'X': 3, 'Y': 5},
        'X': {'A': 3, 'B': 9, 'C': 4, 'D': 2, 'E': 4, 'F': 1, 'G': 5, 'H': 8, 'I': 2, 'J': 3, 'K': 8, 'L': 4, 'M': 5,
              'N': 9, 'O': 4, 'P': 9, 'Q': 8, 'R': 3, 'S': 6, 'T': 7, 'U': 5, 'V': 6, 'W': 3, 'Y': 7},
        'Y': {'A': 6, 'B': 5, 'C': 2, 'D': 7, 'E': 1, 'F': 8, 'G': 3, 'H': 7, 'I': 8, 'J': 2, 'K': 7, 'L': 1, 'M': 6,
              'N': 3, 'O': 5, 'P': 7, 'Q': 4, 'R': 6, 'S': 9, 'T': 3, 'U': 6, 'V': 4, 'W': 5, 'X': 7}
    }

    frozenset_graph_15 = dict_to_frozenset(graph_15)
    frozenset_graph_20 = dict_to_frozenset(graph_20)
    frozenset_graph_25 = dict_to_frozenset(graph_25)
    input_size_options = [frozenset_graph_15, frozenset_graph_20, frozenset_graph_25]
    input_description = ["graph with 15 nodes", "graph with 10 nodes", "graph with 5 nodes"]
    sampling_rate_options = [200]
    """The time Experiment Runner will wait after a run completes.
    This can be essential to accommodate for cooldown periods on some systems."""
    time_between_runs_in_ms:    int             = 60000 # should be 60000, 1minute

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

    # Dynamic configurations can be one-time satisfied here before the program takes the config as-is
    # e.g. Setting some variable based on some criteria
    def __init__(self):
        """Executes immediately after program start, on config load"""
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
        sampling_factor = FactorModel("sampling_rate", self.sampling_rate_options) # Define different sampling intervals
        input_size_factor = FactorModel("input_size", self.input_size_options)  # Define different input sizes
        cache_factor = FactorModel("cache_strategy", self.target_function_names)  # Different cache strategies
        self.run_table_model = RunTableModel(
            factors=[input_size_factor, sampling_factor, cache_factor],
            data_columns=['input_description', 'execution_time','average_cpu_usage','memory_usage','energy_consumption', 'dram_energy', 'package_energy', 'pp0_energy', 'pp1_energy']
        )
        return self.run_table_model

    def before_experiment(self) -> None:
        """Perform any activity required before starting the experiment here
        Invoked only once during the lifetime of the program."""

        remote_experiment_result_dir = f"{self.remote_temporary_results_dir}/{self.name}"
        ssh_cmd = f"ssh {self.remote_user}@{self.remote_host} 'mkdir -p {remote_experiment_result_dir}'"
        try:
            subprocess.run(shlex.split(ssh_cmd), check=True)
            output.console_log(f"Created remote directory: {remote_experiment_result_dir}")
        except subprocess.CalledProcessError as e:
            output.console_log(f"Error creating remote directory: {e}")
            raise e

    def before_run(self) -> None:
        """Perform any activity required before starting a run.
        No context is available here as the run is not yet active (BEFORE RUN)"""
        # packages_dir = os.path.join(self.ROOT_DIR, 'packages')
        pass

    def start_run(self, context: RunnerContext) -> None:
        """Perform any activity required for starting the run here.
        For example, starting the target system to measure.
        Activities after starting the run should also be performed here."""
        """Perform any activity required for starting the run here."""
        remote_temporary_each_run_results_dir = f"{self.remote_temporary_results_dir}/{self.name}/run_{context.run_nr}"
        ssh_cmd = f"ssh {self.remote_user}@{self.remote_host} 'mkdir -p {remote_temporary_each_run_results_dir}'"
        try:
            subprocess.run(shlex.split(ssh_cmd), check=True)
            output.console_log(f"Created remote run directory: {remote_temporary_each_run_results_dir}")
        except subprocess.CalledProcessError as e:
            output.console_log(f"Error creating remote run directory: {e}")
            raise e

    def start_measurement(self, context: RunnerContext) -> None:
        """Start energy measurement using Energibridge."""
        sampling_interval = context.run_variation['sampling_rate']
        target_function = context.run_variation['cache_strategy']
        input_size = context.run_variation['input_size']

        remote_temporary_each_run_results_dir = f"{self.remote_temporary_results_dir}/{self.name}/run_{context.run_nr}"
        python_cmd = (
            f"import sys; import os; import numpy as np; "
            f"sys.path.append('{self.remote_package_dir}'); "
            f"import {self.target_function_location} as module; "
            f"graph = {input_size}; "
            f"module.{target_function}(graph, 'A'); "
        )

        profiler_cmd = (
            f"{self.energibridge_location} --interval {sampling_interval} "
            f"--max-execution 20 "
            f"--output {remote_temporary_each_run_results_dir}/energibridge.csv "
            f"--summary "
            f"python3 -c \"{python_cmd}\" "
        )

        ssh_cmd = f"ssh {self.remote_user}@{self.remote_host} '{profiler_cmd}'"

        energibridge_log = open(f'{context.run_dir}/energibridge.log', 'w')
        self.profiler = subprocess.Popen(shlex.split(ssh_cmd), stdout=energibridge_log, stderr=energibridge_log)

        energibridge_log.write(f'sampling interval: {sampling_interval}, target function: {target_function}, input size: {input_size}\n')
        energibridge_log.flush()
        energibridge_log.close()



    def interact(self, context: RunnerContext) -> None:
        """Perform any interaction with the running target system here, or block here until the target finishes."""
        # No interaction. We just run it for XX seconds.
        # Another example would be to wait for the target to finish, e.g. via `self.target.wait()`
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

        remote_temporary_each_run_results_dir = f"{self.remote_temporary_results_dir}/{self.name}/run_{context.run_nr}"
        local_csv_path = context.run_dir / "energibridge.csv"
        local_log_path = context.run_dir / "energibridge.log"
        remote_csv_path = f"{remote_temporary_each_run_results_dir}/energibridge.csv"

        scp_csv_cmd = f"scp {self.remote_user}@{self.remote_host}:{remote_csv_path} {context.run_dir}"
        try:
            subprocess.run(shlex.split(scp_csv_cmd), check=True)
            output.console_log(
                f"Copied energibridge.csv rom remote directory to local directory: {context.run_dir}")
        except subprocess.CalledProcessError as e:
            output.console_log(f"Error during SCP: {e}")
            return None

        if not local_csv_path.exists():
            output.console_log(f"Error: File {local_csv_path} does not exist!")
            return None

        # energibridge.csv - Power consumption of the whole system
        df = pd.read_csv(local_csv_path)
        run_data = {
            'input_description': self.input_description[ math.ceil(context.run_nr/ (len(self.target_function_names) * len(self.sampling_rate_options))) - 1 ],
            'memory_usage': round(df.get('USED_MEMORY', pd.Series([0])).mean()/(1024 ** 2), 8),
            'dram_energy': round(df.get('DRAM_ENERGY (J)', pd.Series([0])).mean(), 8),
            'package_energy': round(df.get('PACKAGE_ENERGY (J)', pd.Series([0])).mean(), 8),
            'pp0_energy': round(df.get('PP0_ENERGY (J)', pd.Series([0])).mean(), 8),
            'pp1_energy': round(df.get('PP1_ENERGY (J)', pd.Series([0])).mean(), 8),
        }

        # Calculate average CPU usage across all cores
        cpu_columns = [col for col in df.columns if col.startswith('CPU_USAGE_')]
        if cpu_columns:
            core_avg_cpu_usage = df[cpu_columns].mean(axis=0)  # Sum up CPU usage of all cores for each row
            overall_avg_cpu_usage = core_avg_cpu_usage.mean()  # Compute the average CPU usage
            run_data['average_cpu_usage'] = round(overall_avg_cpu_usage, 8)

        if local_log_path.exists():
            try:
                # Implement retry mechanism to handle file read issues
                retries = 5  # Number of retries
                for attempt in range(retries):
                    try:
                        with open(local_log_path, 'r') as log_file:
                            log_content = log_file.read()
                            # Use regular expression to find the execution time in seconds
                            match = re.search(r"Energy consumption in joules: ([\d\.]+) for ([\d\.]+) sec of execution",log_content)
                            if match:
                                run_data['energy_consumption'] = float(match.group(1))  # Extract energy consumption in joules
                                run_data['execution_time'] = float(match.group(2))  # Extract the execution time in seconds
                            else:
                                output.console_log(f"Warning: No energy consumption or execution time found in {local_log_path}")
                                time.sleep(1)  # Wait for 1 second before retrying
                    except IOError:
                        output.console_log(f"Error reading file {local_log_path}. Retrying... ({attempt + 1}/{retries})")
                        time.sleep(1)  # Wait for 1 second before retrying

                if 'execution_time' and 'energy_consumption' not in run_data:
                    output.console_log(f"Error: Unable to retrieve execution time from {local_log_path} after {retries} attempts.")
            except Exception as e:
                output.console_log(f"Exception occurred while reading log file {local_log_path}: {e}")
        else:
            output.console_log(f"Error: Log file {local_log_path} does not exist.")
        return run_data

    def after_experiment(self) -> None:
        """Perform any activity required after stopping the experiment here
        Invoked only once during the lifetime of the program."""
        pass

    # ================================ DO NOT ALTER BELOW THIS LINE ================================
    experiment_path:            Path             = None

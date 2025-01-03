
# %% Import relevant libraries
import os

from __init__ import *


# %% Get data directory
d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# %% Set root directory
os.chdir(os.path.join(d, '..'))

# %% Define directories
ROOT_DIR = os.path.abspath(os.getcwd())
DATA_DIR = os.path.join(ROOT_DIR, "outcomes")
FIGS_DIR = os.path.join(DATA_DIR, "figures")

# %% Print directories
print("project path ➥ " + os.getcwd())

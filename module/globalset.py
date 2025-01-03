
# %% Import relevant libraries
"""
This module sets up the global environment for the project.

It performs the following tasks:
1. Imports necessary libraries and modules.
2. Determines the directory of the current file or the current working directory.
3. Sets the root directory of the project.
4. Defines the root directory as an absolute path.
5. Provides a placeholder for loading data a custom file opener.

Attributes:
    ROOT_DIR (str): The absolute path to the root directory of the project.
"""
import os

from classes import CustomOpen

from __init__ import *


# %% Get data directory
d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# %% Set root directory
os.chdir(os.path.join(d, '..'))

# %% Define directories
ROOT_DIR = os.path.abspath(os.getcwd())

# %% Load Cypher queries
# with CustomOpen(os.path.join(ROOT_DIR, "path-to-some-file")) as f:
#   GLOBALOBJECT = f.read()

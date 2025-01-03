#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import argparse

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'module')))

from __init__ import __version__

from globalset import *

# Global objects
HELPLOG = [
    "Example usage:",
    "❯ python3 python-workflow-template.py",
    " ",
]

# %% Main

def main():
    
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Python project workflow template",
        epilog="\n".join(HELPLOG),
        formatter_class=argparse.RawTextHelpFormatter,
        prog="python-workflow-template",
    )

    # Add version argument
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {__version__}"
    )

    # Clear the terminal screen
    os.system("clear")

    # Define ANSI escape codes for colors
    HEADER_COLOUR = "\033[95m"  # Magenta
    RESET_COLOUR = "\033[0m"  # Reset to default color

    # Print the colourful header line
    columns = os.get_terminal_size().columns
    print(f"{HEADER_COLOUR}{'⎯' * columns}{RESET_COLOUR}")

    # Parse arguments
    args = parser.parse_args()

    
# Check if the script is being run directly
if __name__ == "__main__":
    main()

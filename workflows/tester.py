#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import json
import requests
import datetime
import argparse

from tabulate import tabulate

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'module')))

from __init__ import __version__

from globalset import *
from parser import *

# Global objects
HELPLOG = [
    "Example usage:",
    "❯ python3 tester.py -m",
    "❯ python3 tester.py -s",
    " ",
]

# %% Definitions

def process_stats(meta, stats):
    """
    Process the stats data and display the results.
    """

    # Compile list of systems with stats
    stats_df = pd.json_normalize(stats.values())
    meta_df = pd.json_normalize(meta)
    merged_df = pd.merge(stats_df, meta_df, on='id')

    # Filter data for last 90 days
    selected_columns = merged_df[
        ['id', 'location', 'property', 'age',
         'hp_output', 'hp_model', 'combined_cop', 'combined_data_length']].copy()
    selected_columns.loc[:,
                         'days'] = selected_columns['combined_data_length'] / 86400
    selected_columns.drop(
        columns=['combined_data_length'], inplace=True)
    selected_columns.rename(
        columns={'combined_cop': 'cop'}, inplace=True)
    selected_columns.sort_values(
        by='cop', ascending=False, inplace=True)

    # Print the results
    print("HeatPumpMonitor.org systems (sorted by COP, descending, last 90 days)")
    print(tabulate(selected_columns, headers='keys', tablefmt='psql'))



# %% Main

def main():
    """
    Tester function to check API connection and data.
    """

    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Tester function to check API connection and data",
        epilog="\n".join(HELPLOG),
        formatter_class=argparse.RawTextHelpFormatter,
        prog="api-tester",
    )

    # Add version argument
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {__version__}"
    )

    # Create a group of required arguments [not used]
    required_group = parser.add_argument_group("required named arguments")

    # Create a mutually exclusive group
    exclusive_group = parser.add_mutually_exclusive_group(required=True)

    # Add arguments to the mutually exclusive group
    exclusive_group.add_argument(
        "-m",
        "--metadata",
        dest="meta",
        help="Obtain useful meta fields",
        action='store_true'
    )

    exclusive_group.add_argument(
        "-s",
        "--stats",
        dest="stat",
        help="Obtain useful stats fields",
        action='store_true'
    )

    # Parse arguments
    args = parser.parse_args()
    arg_meta = args.meta
    arg_stat = args.stat
    
    # Clear the terminal screen
    os.system("clear")

    # Define ANSI escape codes for colors
    HEADER_COLOUR = "\033[95m"  # Magenta
    RESET_COLOUR = "\033[0m"  # Reset to default color

    # Print the colourful header line
    columns = os.get_terminal_size().columns
    print(f"{HEADER_COLOUR}{'⎯' * columns}{RESET_COLOUR}")

    # Process each argument and perform the corresponding action
    if arg_meta is True:
        metainfo = fetch_public_devices()
        print(json.dumps(metainfo))
        
    if arg_stat is True:

        # Fetch the data
        meta = fetch_public_devices()
        stats = fetch_public_devices_last_stats()

        # Call the function with the fetched data
        process_stats(meta, stats)
        
    print("\n")


# Check if the script is being run directly
if __name__ == "__main__":
    main()

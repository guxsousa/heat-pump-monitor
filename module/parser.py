import json
import requests
import datetime
import pandas as pd

from globalset import *


def fetch_public_devices(url_base=URL_BASE):
    """
    Fetch the list of public devices from the API.

    Parameters
    ----------
    url_base : str
        The URL of the API.
    
    Returns
    -------
    dict
        The list of public devices.
    """
    url = url_base + '/system/list/public.json'
    response = requests.get(url)
    return response.json()


def fetch_public_devices_last_stats(url_base=URL_BASE):
    """
    Fetch the latest devices with stats from the API.

    Parameters
    ----------
    url_base : str
        The URL of the API.
    
    Returns
    -------
    dict
        The list of public devices.
    """
    url = url_base + '/system/stats/last90'
    response = requests.get(url)
    return response.json()


def get_system_meta(id, url_base=URL_BASE):
    """
    Get the meta data for a system

    Parameters
    ----------
    id : int
        The system ID
    url_base : str
        The base URL for the API
    
    Returns
    -------
    dict
        The meta data for the system
    """
    url = url_base + f"/system/get.json?id={id}"
    response = requests.get(url)
    return response.json()


def get_system_timeseries(id, url_base=URL_BASE):
    """
    Get the available timeseries for a system

    Parameters
    ----------
    id : int
        The system ID
    url_base : str
        The base URL for the API
    
    Returns
    -------
    pd.DataFrame
        A DataFrame with the available timeseries
    """

    # Define the URL to query
    url = url_base + f"/timeseries/available?id={id}"

    # Query the API
    response = requests.get(url)

    # Obtain the json response
    ts_id = response.json()

    # Convert the response to a DataFrame
    ts_id_df = pd.DataFrame.from_dict(ts_id['feeds'], orient='index')
    ts_id_df['start_time'] = pd.to_datetime(ts_id_df['start_time'], unit='s')
    ts_id_df['end_time'] = pd.to_datetime(ts_id_df['end_time'], unit='s')
    ts_id_df.rename(columns={'interval': 'interval__s'}, inplace=True)

    # Return the DataFrame
    return ts_id_df


def fetch_timeseries_data(system_id, feed, start_date, end_date, interval, average, timeformat='notime', url_base=URL_BASE):
    """
    Fetch the timeseries data for a system

    Parameters
    ----------
    system_id : int
        The system ID
    feed : int
        The feed ID
    start_date : str
        The start date
    end_date : str
        The end date
    interval : str
        The interval
    average : str
        The average
    timeformat : str
        The time format
    url_base : str
        The base URL for the API. Default is URL_BASE
    
    Returns
    -------
    dict
        The timeseries data
    """
    url = f"{url_base}/timeseries/data?id={system_id}&feeds={feed}&start={start_date}&end={end_date}&interval={interval}&average={average}&timeformat={timeformat}"
    response = requests.get(url)
    timeseries = response.json()

    # Generate date_time column
    start_date = datetime.datetime.strptime(start_date, '%d-%m-%Y')
    end_date = datetime.datetime.strptime(end_date, '%d-%m-%Y')
    date_range = pd.date_range(start=start_date, end=end_date, freq=f'{interval}s')

    # Create dataframe
    timeseries_df = pd.DataFrame(
        {'id': system_id, 'datetime': date_range, 'value': timeseries[feed], 'feed': feed})
    
    return timeseries_df

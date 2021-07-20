"""
@author: Ademola Olokun
"""

import sys
import json
import pandas as pd
from datetime import datetime

"""
A python script thats reads in file, 
checks if an item is expired and tags either with 'True' or 'False'
and returns the processed output in JSON format.
"""


def read_file():
    """
    Function to read in filepath from command line

    Returns: 
        input_data (dataframe): returns the input data as dataframe
    """
    fpath = input("Input Filepath: ")
    input_data = pd.read_csv(fpath, parse_dates=['date'])

    return input_data


def obsolete(exp_date):
    """
    This function checks if an item's expiry date was before 2020-01-01 or not

    Args:
        exp_date (datetime): expiry date of items from the input file

    Returns:
        True or False (boolean)
    """
    ref_exp_date = pd.to_datetime("2021-01-01")  # reference expiry date
    diff = (exp_date - ref_exp_date).days

    if diff < 0:
        return 'True'
    else:
        return 'False'


def add_column(data):
    """
    Adds new column 'obsolete' with value either 'True' or 'False',
    if an item is expired or not

    Args:
        data (dataframe): input data from read_file()

    Returns:
        processed_data (dataframe): processed dataframe with the new column
    """

    data['obsolete'] = data['date'].map(obsolete)
    processed_data = data

    return processed_data


def output_json(data):
    """
    Converts dataframe into JSON format.

    Args:
        data (dataframe): input dataframe from obsolete()
    """
    try:
        output_json = data.to_json(orient='records')

        with open('data_output.json', 'w') as outfile:
            json.dump(output_json, outfile)

        print('JSON file created in directory!')
    except Exception:
        print('Error creating as JSON file!')


def main():
    try:
        input_data = read_file()
        processed_data = add_column(input_data)
        output_json(processed_data)
    except IOError:
        print('Could not read in file. Re-check filename or add filepath.')


if __name__ == '__main__':
    main()

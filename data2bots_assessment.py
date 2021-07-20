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


def main_function(data):
    """
    This function checks if an item's expiry date was before 2020-01-01 
    and adds the result ('True' or 'False') in the 'obsolete' column.

    Args:
        data (dataframe): input dataframe from read_file()

    Returns:
        processed_data (dataframe): processed dataframe with 'obsolete' column
    """
    expiry_date = pd.to_datetime("2021-01-01")

    data['obsolete'] = [True if data.loc[row, 'date'] <
                        expiry_date else False for row in range(len(data))]
    processed_data = data

    return processed_data


def output_json(data):
    """
    Converts dataframe into JSON format.

    Args:
        data (dataframe): input dataframe from main_function()
    """
    output_json = data.to_json(orient='records')

    with open('output.json', 'w') as outfile:
        json.dump(output_json, outfile)

    print('JSON file created!')


def main():
    try:
        input_data = read_file()
        processed_data = main_function(input_data)
        output_json(processed_data)
    except IOError:
        print('Could not read in file. Re-check filename or add filepath.')


if __name__ == '__main__':
    main()

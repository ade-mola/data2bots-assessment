"""
@author: Ademola Olokun
"""

from data2bots_assessment import obsolete
import pandas as pd

def test_obsolete_true():
    """
    tests that obsolete function returns 'True'
    when a date less than 2021-01-01 is passed
    """
    date = pd.to_datetime('2020-09-01')
    result = obsolete(date)
    assert result == True


def test_obsolete_false():
    """
    tests that obsolete function returns 'False'
    when a date greater than 2021-01-01 is passed
    """
    date = pd.to_datetime('2021-07-12')
    result = obsolete(date)
    assert result == False

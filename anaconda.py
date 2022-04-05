import pandas as pd
import pytest


def test_data():
    df = pd.read_csv(r'C:\Users\0035R2744\Desktop\Employee.csv')
    data = df.columns
    Region = 'Region'
    assert True
    assert Region in data

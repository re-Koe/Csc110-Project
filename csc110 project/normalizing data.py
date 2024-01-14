"""Test doc
"""
from backend import load_data, Month
from sklearn import preprocessing
import datetime
import pandas as pd
import numpy as np


import scipy


dummy_data = load_data(datetime.date(2020, 3, 1), datetime.date(2021, 10, 1), True)

x_array = np.array([mo.covid_cases for mo in dummy_data])
normalized_arr = preprocessing.normalize([x_array])
normalized_arr = normalized_arr[0]

print([number / scipy.linalg.norm(x_array) for number in x_array])
print(normalized_arr)

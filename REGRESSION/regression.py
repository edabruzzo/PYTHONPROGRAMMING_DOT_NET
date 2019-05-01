'''
https://pythonprogramming.net/regression-introduction-machine-learning-tutorial/https://pythonprogramming.net/machine-learning-python-sklearn-intro

COMMAND FOR EXECUTION: 

    C:/Users/Emm/AppData/Local/Programs/Python/Python37-32/python.exe regression.py

'''

import quandl, math
import numpy as np
import pandas as pd


'''
cross_validation is deprecated since version 0.18. This module will be removed in 0.20. Use sklearn.model_selection.train_test_split instead.
'''
#from sklearn import preprocessing, cross_validation, svm


from sklearn.model_selection import cross_validate
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression



df = quandl.get("WIKI/GOOGL")
df = df[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

print(df.head());
print(df.tail())

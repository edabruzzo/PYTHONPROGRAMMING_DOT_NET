'''
https://pythonprogramming.net/regression-introduction-machine-learning-tutorial/https://pythonprogramming.net/machine-learning-python-sklearn-intro

COMMAND FOR EXECUTION: 

    C:/Users/Emm/AppData/Local/Programs/Python/Python37-32/python.exe c/Users/Emm/Documents/NetBeansProjects/PYTHONPROGRAMMING_DOT_NET/REGRESSION
/regression.py

'''





import pandas as pd
import quandl

df = quandl.get("WIKI/GOOGL")

df = df[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']]

'''
This creates a new column that is the % spread based on the closing price, which is our crude measure of volatility. Next, we'll do daily percent change:
'''
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100.0

'''
I went ahead and recorded the video version of this, not realizing my stake that it was high minus low divided by close. I meant to do High - Low, divided by the low. Feel free to fix that if you like.

This creates a new column that is the % spread based on the closing price, which is our crude measure of volatility. Next, we'll do daily percent change:

'''
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0;

#Now we will define a new dataframe as:
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

print(df.head());
print(df.tail())

'''
https://pythonprogramming.net/regression-introduction-machine-learning-tutorial/https://pythonprogramming.net/machine-learning-python-sklearn-intro



'''





import pandas as pd
import quandl

df = quandl.get("WIKI/GOOGL")

df = df[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']]

'''
This creates a new column that is the % spread based on the closing price, which is our crude measure of volatility. Next, we'll do daily percent change:
'''
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close'] * 100.0

#Now we will define a new dataframe as:

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

print(df.head());
print(df.tail())

'''
https://pythonprogramming.net/regression-introduction-machine-learning-tutorial/https://pythonprogramming.net/machine-learning-python-sklearn-intro

COMMAND FOR EXECUTION: 

    C:/Users/Emm/AppData/Local/Programs/Python/Python37-32/python.exe regression.py



TO USE QUANDL YOU HAVE TO REGISTER 

THERE'S A LIMIT FOR ANONYMOUS REQUESTS (50 CALLS PER DAY)
To make more calls today, please register for a free Quandl account and then include your API key with your requests.

https://docs.quandl.com/docs/getting-started

https://docs.quandl.com/docs/getting-started#section-authenticating-your-requests


I'VE CREATED A QUANDL KEY FOR REQUESTS AND SET IT TO ENVIRONMENT VARIABLE



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
from sklearn.model_selection import train_test_split

import os


df = quandl.get("WIKI/GOOGL", api_key=os.environ['QUANDL_KEY'])
df = df[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

#That's the label that we want to predict/forecast
forecast_col = 'Adj. Close'
df.fillna(value=-99999, inplace=True)

#previsão de 1 dia no futuro
forecast_out = int(math.ceil(0.01 * len(df)))

#Adicional a coluna 'label' para fazer a predição
df['label'] = df[forecast_col].shift(-forecast_out)

#Drop any additional Nan value from dataframe
df.dropna(inplace=True)

X = np.array(df.drop(['label'], 1))
#It keeps our trainning dataset in a range between -1 and 1
X = preprocessing.scale(X)

y = np.array(df['label'])



'''

HERE IS VERY ADVISABLE TO READ THE DOCUMENTATION OF THE SCIKIT-LEARN
READ THE FILE ITSELF AND THE OFFICIAL SITE OF SCIKIT-LEARN



file:///C:/Users/Emm/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/sklearn/model_selection/_validation.py

https://scikit-learn.org/stable/modules/cross_validation.html

'''
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)


classificador1 = svm.SVR();
#conjunto de treinamento - treinando modelo
classificador1.fit(X_train, y_train);

#Here, we're "fitting" our training features and training labels.
#Our classifier is now trained. Wow that was easy. Now we can test it!

confidence = classificador1.score(X_test, y_test)
print(confidence)


from sklearn.datasets import load_boston
from sklearn import datasets, linear_model
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, mean_absolute_error, median_absolute_error
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.model_selection import cross_val_predict
import numpy as np
import pandas as pd
import statsmodels.api as sm
import sys

def clear():
    sys.stderr.write("\x1b[2J\x1b[H")
    

def metrics(test, predictions):
    return_mean_squared_error = mean_squared_error(test, predictions)
    return_mean_absolute_error = mean_absolute_error(test, predictions)
    return_median_absolute_error = median_absolute_error(test, predictions)

    print("ERRO MEDIO QUADRADO: %.2f" % return_mean_squared_error)
    print("ERRO MEDIO ABSOLUTO: %.2f" % return_mean_absolute_error)
    print("ERRO MEDIANO ABSOLUTO: %.2f" % return_median_absolute_error)
    print("\n")

    return mean_squared_error, mean_absolute_error, median_absolute_error

def linear_regression_simple(data, index, feature_name):

    #get only one feature (in this case number of rooms)
<<<<<<< HEAD
    data_x = data.data[:, np.newaxis, 5]
    target = data.target
    # data_x = data_x[0:100]
=======
    data_x = data.data[:, np.newaxis, index]
>>>>>>> 7e23e80adf251a8b473cf72f90ad3a26cf9763c4

    qtd_train = 350

    #split data in train and test
    x_train = data_x[0:qtd_train + 1]
    x_test  = data_x[qtd_train + 1:last_position]

    y_train = target[0:qtd_train + 1]
    y_test  = target[qtd_train + 1:last_position]
    
    #creating model
    regr = linear_model.LinearRegression()
    regr.fit(x_train, y_train)

    y_predictions = regr.predict(x_test)

    print("FEATURE ANALISADA: %s" % feature_name)
    
    metrics(y_test, y_predictions)


data = load_boston()

#EXECUTANDO REGRESSÃO LINEAR SIMPLES
print ("Regressão Simples")
count = 0
for feature in data.feature_names:
    linear_regression_simple(data, count, feature)
    count = count + 1


from sklearn.datasets import load_boston
from sklearn import datasets, linear_model
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, mean_absolute_error, median_absolute_error
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import sys

def clear():
    sys.stderr.write("\x1b[2J\x1b[H")

def linear_regression(data):

    #get only one feature (in this case number of rooms)
    data_x = data.data[:, np.newaxis, 5]

    qtd_train = 350

    #split data in train and test
    x_train = data_x[0:qtd_train + 1]
    x_test  = data_x[qtd_train + 1:]

    y_train = data.target[0:qtd_train + 1]
    y_test  = data.target[qtd_train + 1:]
    
    #creating model
    regr = linear_model.LinearRegression()
    regr.fit(x_train, y_train)

    y_predictions = regr.predict(x_test)

    #print("FEATURE ANALISADA: %s" % feature)
    print('Coefficients: \n', regr.coef_)

    print("ERRO MEDIO QUADRADO: %.2f" % mean_squared_error(y_test, y_predictions))
    print("ERRO MEDIO ABSOLUTO: %.2f" % mean_absolute_error(y_test, y_predictions))
    print("ERRO MEDIANO ABSOLUTO: %.2f" % median_absolute_error(y_test, y_predictions))
    print("\n")
    #count = count + 1

    # Plot outputs
    plt.scatter(x_test, y_test,  color='black')
    plt.plot(x_test, y_predictions, color='blue', linewidth=3)
    plt.xlabel("QTD MEDIA DOS QUARTOS")
    plt.ylabel("PRECO MEDIO DAS CASAS")

    plt.xticks(())
    plt.yticks(())

    plt.show()
    

linear_regression(load_boston())
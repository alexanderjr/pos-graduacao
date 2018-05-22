from sklearn.datasets import load_boston
from sklearn import datasets, linear_model
from sklearn import linear_model
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import sys

#https://gist.github.com/sanguedemonstro/53071059def69958a97098c41e2e0e51

def clear():
    sys.stderr.write("\x1b[2J\x1b[H")

def summary(data):
    data_frame = pd.DataFrame(data.data, columns=data.feature_names)
    target = pd.DataFrame(data.target, columns=["MEDV"])

    x = data_frame["RM"]
    y = target["MEDV"]

    model = sm.OLS(y,x).fit()
    predictions = model.predict(x)

    model.summary()

def linear_regression(data):

    # #get all data from specific position data and features
    # features = [data.feature_names[0], data.feature_names[5]]
    # feature_data = data.data[0:, [0,5]]

    # #dataframe with values and columns
    # df = pd.DataFrame(feature_data, columns=features)
    # #df = pd.DataFrame(data.data, columns=data.feature_names)
    
    # #dataframe with target values
    # target = pd.DataFrame(data.target, columns=["MEDV"])

    # #instance of LinearRegression ML
    # lm = linear_model.LinearRegression()
    
    # #fit our model
    # model = lm.fit(df,target["MEDV"])
    
    # #make predictions
    # predictions = lm.predict(df)

    # print "SCORE:"
    # print (lm.score(df, target["MEDV"]))
    # print "COEFICIENTE :"
    # print (lm.coef_)
    
    diabetes = datasets.load_diabetes()

    print diabetes.feature_names
    diabetes_X = diabetes.data[:, np.newaxis, 2]
    print diabetes_X

    exit()

    data_X = data.data[:, np.newaxis,2]

    print len(data_X)

    exit()

    qtd_train = 350

    x_train = data.data[0:qtd_train + 1]
    x_test  = data.data[qtd_train + 1:]

    y_train = data.target[0:qtd_train + 1]
    y_test  = data.target[qtd_train + 1:]

    regr = linear_model.LinearRegression
    

linear_regression(load_boston())

# 1 - Escolher uma feature para avaliar coeficiente de determinação, a fim de verificar se existe uma relação entrea a variável de entrada com a de saída (target)

# 2 - Após avaliar, escolher

#https://towardsdatascience.com/simple-and-multiple-linear-regression-in-python-c928425168f9

#https://towardsdatascience.com/a-quick-introduction-to-the-pandas-python-library-f1b678f34673

#http://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html
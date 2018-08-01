import pandas as pd
import matplotlib as plt
import numpy as np
from sklearn import tree
from sklearn.cross_validation import train_test_split

movies = pd.read_csv('datasets/avaliacoes_usuario.csv')

features = movies[movies.columns[1:16]]
target = movies[movies.columns[16:]]

X_train, X_test, Y_train, Y_test = train_test_split(features, target, test_size=0.2)

X_train = np.array(X_train).reshape(len(X_train), 15)
X_test = np.array(X_test).reshape(len(X_test), 15)

Y_train = Y_train.values.ravel()
Y_test = Y_test.values.ravel()

modelo = tree.DecisionTreeRegressor()
modelo.fit(X_train, Y_train)

modelo.score(X_train, Y_train)
modelo.score(X_test, Y_test)
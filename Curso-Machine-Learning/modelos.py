import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, median_absolute_error, mean_absolute_error
from sklearn import tree

def run_model(dataset, model):    
    movies = pd.read_csv(dataset)

    features = movies[movies.columns[1:16]]
    target = movies[movies.columns[16:]]

    X_train, X_test, Y_train, Y_test = train_test_split(features, target, test_size=0.2)

    X_train = np.array(X_train).reshape(len(X_train), 15)
    X_test = np.array(X_test).reshape(len(X_test), 15)

    Y_train = Y_train.values.ravel()
    Y_test = Y_test.values.ravel()

    model.fit(X_train, Y_train)

    Y_predict = model.predict(X_test)

    score_train = model.score(X_train, Y_train)
    score_test = model.score(X_test, Y_test)
    score_predict = model.score(X_test, Y_predict)

    print("Score Train")
    print(score_train)

    print("Score Test")
    print(score_test)

    print("Score Predict")
    print(score_predict)

    return score_train, score_test, score_predict

dataset = 'datasets/avaliacoes_usuario.csv'

print("Modelo LogisticRegression")
run_model(dataset, LogisticRegression()) 
print("\n")
print("Modelo DecisionTreeRegressor")
run_model(dataset, tree.DecisionTreeRegressor(max_depth=5))
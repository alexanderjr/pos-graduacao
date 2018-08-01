import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, median_absolute_error, mean_absolute_error
from sklearn.model_selection import cross_val_score

movies = pd.read_csv("datasets/movies_multilinear_reg.csv")

filmes_independentes = movies[movies.columns[2:17]]
filmes_dependentes = movies[movies.columns[17:]]

X_train, X_test, Y_train, Y_test = train_test_split(filmes_independentes, filmes_dependentes, test_size=0.3)

X_train = np.array(X_train).reshape(len(X_train), 15)
X_test = np.array(X_test).reshape(len(X_test), 15)

modelo = LinearRegression()

#cross validation ou k-fold validation
score = cross_val_score(modelo, filmes_independentes, filmes_dependentes,cv=10,scoring=)


modelo.fit(X_train, Y_train)

Y_predict = modelo.predict(X_test)

# print "Erro médio Absoluto"
# print modelo.score(X_test, Y_predict)

# print "\n"

print "Coeficiente de Determinação"
print r2_score(Y_test, Y_predict)

print "\n"

print "Erro médio absoluto"
print mean_absolute_error(Y_test, Y_predict)

print "\n"

print "Erro mediano absoluto"
print median_absolute_error(Y_test, Y_predict)

print "\n"

print "Erro médio quadrado"
print mean_squared_error(Y_test, Y_predict)




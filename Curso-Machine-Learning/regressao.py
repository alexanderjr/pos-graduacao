import pandas as pd
import matplotlib.pyplot as plt
# import sklearn.model_selection as train_test_split
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
from sklearn.linear_model import LinearRegression

movies = pd.read_csv("datasets/regressao_linear_alura.csv")

# sample = movies.sample(n=200)
# x = sample["Investimento (em milhoes)"]
# y = sample["Bilheteria (pessoas)"]

# plt.scatter(x,y)
# plt.xlabel("Investimento (em milhoes)")
# plt.ylabel("Bilheteria (pessoas)")
# plt.show()

filmes_investimento = movies["Investimento (em milhoes)"]
filmes_bilheteria = movies["Bilheteria (pessoas)"]

X_treino, X_teste, Y_treino, Y_teste = train_test_split(filmes_investimento, filmes_bilheteria)

X_treino = np.array(X_treino).reshape(len(X_treino),1)
X_teste = np.array(X_teste).reshape(len(X_teste),1)
Y_treino = np.array(Y_treino).reshape(len(Y_treino),1)
Y_teste = np.array(Y_teste).reshape(len(Y_teste),1)

modelo = LinearRegression()
modelo.fit(X_treino, Y_treino)
Y_predict = modelo.predict(X_teste)

print r2_score(Y_teste,Y_predict)
print modelo.score(X_teste, Y_teste)

#INVESTIMENTO EM MILHOES
# zootopia = 27.74456356
# print modelo.predict(zootopia)
# print modelo.coef_* zootopia + modelo.intercept_

# print "y = mx + b\n"

# print "COEFICIENTE ANGULAR:" 
# print modelo.coef_

# print "\n"

# print "COEFICIENTE LINEAR:" 
# print modelo.intercept_

# print "\n"

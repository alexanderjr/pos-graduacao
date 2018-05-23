from sklearn import datasets

iris_dict = datasets.load_iris()

#dicionario com as chaves
iris_dict.keys()

#dados
print iris_dict["data"]

#label de cada valor dpos objetos
print iris_dict["feature_names"]

#valores alvo
print iris_dict["target"]

#classe do objeto de cada target
print iris_dict["target_names"]






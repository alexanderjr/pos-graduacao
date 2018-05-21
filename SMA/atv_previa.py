from sklearn.datasets import load_boston
from matplotlib import pyplot as plt

import sys

#https://gist.github.com/sanguedemonstro/53071059def69958a97098c41e2e0e51

def clear():
    sys.stderr.write("\x1b[2J\x1b[H")

boston = load_boston()

#dados da primeira casa (na mesma ordem de feature_names)
boston.data[:1]

#labels dos valores do primeiro item
boston.feature_names

#valores alvos
boston.target

#dados da primeira feature de todos os elementos (primeira coluna de feature_names)
boston.data[:, :8]

#posicao da distancia dos grandes centros
#print boston.data[:1][0][7]


# print boston.target[:2]

print boston.data[:, :9]

exit()

plt.plot(boston.target, boston.data[:, :9], color='green', marker='o', linestyle='solid')
# plt.title("Relacao Valor casa X Distancia grandes centros de trabalho")
plt.ylabel("Distancia dos grandes centros")
plt.xlabel("Valor Casa")

plt.show()


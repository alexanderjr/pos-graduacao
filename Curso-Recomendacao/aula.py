from math import sqrt

avaliacoes = {'Ana': 
		{'Freddy x Jason': 2.5, 
		 'O Ultimato Bourne': 3.5,
		 'Star Trek': 3.0, 
		 'Exterminador do Futuro': 3.5, 
		 'Norbit': 2.5, 
		 'Star Wars': 3.0},
	 
	  'Marcos': 
		{'Freddy x Jason': 3.0, 
		 'O Ultimato Bourne': 3.5, 
		 'Star Trek': 1.5, 
		 'Exterminador do Futuro': 5.0, 
		 'Star Wars': 3.0, 
		 'Norbit': 3.5}, 

	  'Pedro': 
	    {'Freddy x Jason': 2.5, 
		 'O Ultimato Bourne': 3.0,
		 'Exterminador do Futuro': 3.5, 
		 'Star Wars': 4.0},
			 
	  'Claudia': 
		{'O Ultimato Bourne': 3.5, 
		 'Star Trek': 3.0,
		 'Star Wars': 4.5, 
		 'Exterminador do Futuro': 4.0, 
		 'Norbit': 2.5},
				 
	  'Adriano': 
		{'Freddy x Jason': 3.0, 
		 'O Ultimato Bourne': 4.0, 
		 'Star Trek': 2.0, 
		 'Exterminador do Futuro': 3.0, 
		 'Star Wars': 3.0,
		 'Norbit': 2.0}, 

	  'Janaina': 
	     {'Freddy x Jason': 3.0, 
	      'O Ultimato Bourne': 4.0,
	      'Star Wars': 3.0, 
	      'Exterminador do Futuro': 5.0, 
	      'Norbit': 3.5},
			  
	  'Leonardo': 
	    {'O Ultimato Bourne':4.5,
             'Norbit':1.0,
	     'Exterminador do Futuro':4.0}
}

def distacia_euclidiana(usuario1, usuario2):
    si = {}
    for key in avaliacoes[usuario1]:
        if key in avaliacoes[usuario2]:
            si[key] = 1
    
    if len(si) == 0: return 0

    soma = 0

    for item in avaliacoes[usuario1]:
        if item in avaliacoes[usuario2]:
            soma = soma + pow((avaliacoes[usuario1][item] - avaliacoes[usuario2][item]),2)

    # soma = sum([pow(avaliacoes[usuario1][item] - avaliacoes[usuario2][item],2) for item in avaliacoes[usuario1] if item in avaliacoes[usuario2]])

    return 1/(1 + sqrt(soma))

resultado = distacia_euclidiana('Leonardo', 'Ana')    

# print(resultado)

usuario_alvo = 'Pedro'

for usuario in avaliacoes:
	if usuario != usuario_alvo:
		resultado = distacia_euclidiana(usuario_alvo, usuario)
		print('{0} - {1}'.format(usuario, resultado))

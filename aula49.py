"""
For in com listas
"""
lista = ['Maria' , 'Helena', 'Luiz']

for nome in lista :
    print(nome, type(nome))

lista_2 = ['vermelho', 'preto', 'branco']
for indice, valor in enumerate(lista_2):
    print(f'{indice} {valor}')

lista_3 = ['galo', 'america', 'palmeiras']
indices = range(len(lista_3))
for indice in indices:
    print(indice, lista_3[indice], type(lista_3[indice]))
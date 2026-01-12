"""
enumerate - enumera iteráveis (índeces)
"""
#
lista = ['Maria', 'Helena', 'Luiz']
lista.append('joão')

for indice, nome in enumerate(lista) :
    print(indice, nome, lista[indice])
    
#for item in enumerate (listas) :
#   indice, nome = item
#   print(indice, nome)


#for tupla_enumerada in enumerate(listas):
#   print('for da tupla:')
#   for valor in tupla_enumerada :
#       print(f'\t {valor}')


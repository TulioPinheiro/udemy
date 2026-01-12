"""  While/else  """
"""Toda vez que o encontramos uma palavra break 'else nao sera executado'"""
""" e toda vez que o laço vai ate o final o laço sera executado"""
string = 'Valor qualquer'

i = 0 
while i < len (string) :
    letra = string[i]

    print(letra)
    i += 1
else:
    print('não encontrei um espaço na string ')
print('Fora do while')
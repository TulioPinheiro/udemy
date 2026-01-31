# Função lambda em Pyhton
# A função lambda é uma função como qualquer 
# outra em Python . Porém , são funções anônimas
# que contém apenas uma linha. Ou seja , tudo
# deve ser contido dentro de uma única 
# expressão .
# lista = [
#   {'nome': 'Túlio', 'sobrenome': 'Pinheiro'},
#   {'nome': 'Ana', 'sobrenome': 'Silva'},
#   {'nome': 'João', 'sobrenome': 'Santos'},
#   {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#   {'nome': 'Pedro', 'sobrenome': 'Almeida'},
# ]
#  
#lista = [4, 31, 1, 22, 3, 4, 6, 10]
#lista.sort()
#sorted(lista)
lista = [
   {'nome': 'Túlio', 'sobrenome': 'Pinheiro'},
   {'nome': 'Ana', 'sobrenome': 'Silva'},
   {'nome': 'João', 'sobrenome': 'Santos'},
   {'nome': 'Maria', 'sobrenome': 'Oliveira'},
   {'nome': 'Pedro', 'sobrenome': 'Almeida'},
 ]

#def orderna(item):
#    return item['sobrenome']

#lista.sort(kry=lambda item: item['sobrenome'])
def exibir(lista):
    for item in lista:
        print(item)
    print()
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])
#lista.sort()
#print(lista)

exibir(l1)
exibir(l2)
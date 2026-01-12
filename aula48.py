"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo 
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis : 
    append = Adiciona um item ao final  
    insert = Adiciona um item no indice escolhido
    pop = Remove do final ou do indice escolhido 
    del = Apaga um indice
    clear = Limpa a lista 
    extend = estende a lista 
    + - = concatena listas 
Create Read Update      Delete
Criar, ler, alterar,    apagar = lista[i] (CRUD)
"""


#          +01234
#          -54321
#string = 'ABCDE' # 5 caracteres(len)
#lista = [] # ''
#print(bool(lista)) # falsy
#print (lista, type(lista))

#         0   1      2             3    4
#        -5   -4     -3           -2   -1
#lista = [123, True, 'Luiz Otávio',1.2, []]
#lista[-3] = 'Maria'
#print(lista)
#print(lista[2], type(lista[2]))

#        0  1   2    3
lista = [10, 20, 30, 40]
#lista.append('Luiz')
#nome = lista.pop()
#lista.append(1233)
#del lista[-1]
#lista.clear()
#print(lista)
#lista [2] = 300
#del lista[2]
#print(lista)
#print(lista[2])
#lista.insert(0, 5) inseri numero na lista ou uma string
#print(lista(5))
lista.append(50) #adiciona numero na lista
lista.pop() #remove o ultimo elemento adicionado na lista
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, ' Removido , ', ultimo_valor)
print(lista)

#lista_a = [1, 2, 3]
#lista_b = [4, 5, 6]
#lista_c = lista_a + lista_b
#lista_a.extend(lista_b)
#print(lista_a)


"""
cuidados com dados mutáveis
 = - copiado o valor (imutáveis)
 = - aponta para o mesmo valor na memória (mutável)
 """

#nome = 'luiz'
#noutra_variavel = nome
#nome = 'joao'
#print(nome)
#print(noutra_variavel)

#lista_a = ['Luiz', 'Maria' , 1, True, 1.2]
#lista_b = lista_a.copy()

#lista_a[0] = 'Qualquer coisa'
#print(lista_a)
#print(lista_b)

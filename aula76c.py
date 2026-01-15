# Métodos úteis dos dcionários em Python
# Len - quantas chaves
# Keys - iteráveis com as chaves
# Values - iterável com os valores
# Items - iterável com chaves e valores
# Setdefault - adiciona valor se a chave não existe
# Copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com especificada (del)
# popitem - Apaga o último item adiconado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Túlio',
    'sobrenome': 'Pinheiro',
    'idade': 32,
}

pessoa.setdefault('idade', 0)
print(pessoa['idade'])
#print(len(pessoa))
#print(list(pessoa.keys()))
#print(list(pessoa.values()))
#print(list(pessoa.items()))

#for valor in pessoa.values():
#    print(valor)

#for chave, valor in pessoa.items():
#    print(chave, valor)

d1 = {
    'c1' : 1,
    'c2' : 2,
    'l1' : [0, 1, 2],
}
d2 = d1.copy() # cópia rasa (shallow copy) 
#d2 = copy.deepcopy(d1) # cópia profunda (deep copy)
d2['l1'][1] = 9999

d2['c1'] = 1000
print(d1)
print(d2)


p1 = {
    'nome': 'Túlio',      
    'sobrenome': 'Pinheiro',
}
#print(p1.get('nome'))
#print(p1.get('nome', 'Não existe'))

#nome = p1.pop('nome')
#print(nome)
#print(p1)
ultima_chave = p1.popitem() #remove a ultima chave do dicionário
print(ultima_chave)
print(p1)

p1 .update({
    'nome' : 'Annie',
    'idade': 25
})
p1.update(nome ='novo valor ', idade = 30)
tupla = ('nome ', 'novo valor') , ('idade', 41)
lista = [ ['nome ', 'outro valor'] , ['idade', 50] ]
p1.update(lista)
p1.update(tupla)
print(p1)
#Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'nome'

pessoa['nome'] = 'Túlio'
pessoa['sobrenome'] = 'Pinheiro'

print(pessoa[chave])

pessoa[chave] = 'Annie'

del pessoa['sobrenome']

print(pessoa)
print(pessoa['nome'])

print( pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is not None:
    print('Não existe ')
else:
    print(pessoa['sobrenome'])



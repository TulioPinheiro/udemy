#video 121
# dicionari em python ( tipos disct)
#Dicionarios são estruturas de dados do tipo
#par de "chave" e de "valor"
#Chaves podem ser consideradas como o "índece"
# que vimos na lista e podem ser de tipos imutáveis
# como : str, int, float, bool, tuple, etc.
#O valor pode ser de qualquer tipo, incluido outro 
#dicionario.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis : str, int, float, bool, tuple
# Mutáveis : list, dict
pessoas = {
    'nome': 'Túlio',
    'sobrenome': 'Pinheiro',
    'idade': 32,
    'altura': 1.74,
    'endereço': [
       { 'rua': 'tal tal', 'numero': 123 },
       { 'rua': 'outra rua', 'numero': 456 }
     ],
}
#print(pessoas, type(pessoas))
print(pessoas['nome'])
print(pessoas['sobrenome'])

print()

for chave in pessoas :
    print(chave, pessoas[chave])



#pessoa = dict(nome ='Túlio ', sobrenome='Pinheiro')
#pessoa = {
#   'nome': 'Tulio',
#    'sobrenome': 'Pinheiro',
#}
# print(pessoa, type(pessoa))


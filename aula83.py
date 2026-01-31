# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
print(a, b)


#a, b = pessoa.values()
#a, b = pessoas.items()
#(a1, a2), (b1, b2) = pessoa.items()
#print (a1, a2)
#print (b1, b2)
#print(a, b)

#for chave, valor in pessoa.items():
#    print(chave, valor)
pessoa = {
    'nome': 'Túlio',
    'sobrenome': 'Pinheiro',
}

dados_pessoa = {
    'idade': 32,
    'cidade': 'Belo Horizonte',
}

pessoa_completa = {**pessoa, **dados_pessoa}
#print(pessoa_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados))

def mostro_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(nome='Túlio', qlq=123)
mostro_argumentos_nomeados(**pessoa_completa)

# configuracoes = {
#    'arg1': 1,
#    'arg2': 2,
#    'arg3': 3,
#     'arg4': 4,
# }
# mostro_argumentos_nomeados(**configuracoes)
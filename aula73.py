"""
Higher Order Functions (Funções de Alta Ordem)
Funções de primeira classe
"""

def saudacao(msg, nome):
    return f"{msg}, {nome}!"

def executa(funcao, *args):
    return funcao(*args)

print(
    executa(saudacao, "Bom dia", "Tulio")
    )
print(
    executa(saudacao, "Boa tarde", "Maria")
    )

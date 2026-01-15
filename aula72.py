#aula 114
""" Exercícios com funções
Crie uma função que multiplica todos os argumentos
não nomeados recebidos 
retorne o total para uma variável e mostre o valor
da variável."""

def multiplica (*args):
    total = 1
    for numero in args:
        total *= numero
    return total
multiplicacao = multiplica (1, 2, 3, 4, 5)
print(multiplicacao)



#Crie uma fução fala se um número é par ou impar
#Retorne se o número é par ou impar

def par_ou_impar (numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'O número {numero} é par'
    #else: não necessario ser utilizado nesse caso
    return f'O número {numero} é impar' 
    
print(par_ou_impar(7))
print(par_ou_impar(4))
print(par_ou_impar(15))
print(par_ou_impar(10))
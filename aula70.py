"""
Retorno de  valores das funções (return)
"""

def soma (x, y) :
    if x > 10 :
        return [10, 20] # apenas um returno por funcao
    return x + y #apenas função e metodo que retornam return

#ariavel = soma(1, 2)
#ariavel = int('1')
soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma1 + soma2)
print (soma(10, 50))
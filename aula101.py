# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y

def multiplicar(x, y):
    return x * y

def executa(funcao, *args): #def executa(funcao, x)
    #def interna(y):
    return funcao (*args) #return funcao(x, y)
    #return interna

soma_com_cinco = executa(lambda x: soma(x, 5), 10)
multiplica_por_dez = executa(lambda x: multiplicar(x, 10), 10)



print(soma_com_cinco)
print(multiplica_por_dez)



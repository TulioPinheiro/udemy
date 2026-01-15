# Exercícios
# crias funções que duplicam, triplicam e quadruplicam
# o valor recebido como parâmetro

def duplicar(valor):
    return valor * 2
def triplicar(valor):
    return valor * 3  
def quadruplicar(valor):
    return valor * 4
def calcular(funcao, valor):
    return funcao(valor)
print(calcular(duplicar, 5))
print(calcular(triplicar, 5))   
print(calcular(quadruplicar, 5))
#print(calcular(lambda x: x * 5, 5))  # Função anônima para quintuplicar

#def criar_multiplicador(multiplicador):
#    def multiplicar(valor):
#        return valor * multiplicador
#    return multiplicar

#duplicar = criar_multiplicador(2)
#triplicar = criar_multiplicador(3) 
#quadruplicar = criar_multiplicador(4)

#print(duplicar(5))
#print(triplicar(5))
#print(quadruplicar(5))


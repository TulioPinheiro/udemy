"""
Argumentos nomeados e não nomeados em funções em Python
Argumentos nomeado tem nome com sinal de igual
Argumentos não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z): #parametros  x,y definiçao de funcao def
    #Definição
    print(f'{x=} +y={y}', '|', 'x+y+z', x+y+z)

#nome da funçao SOMA
soma(1, 2, 3) #argumento pocisional # EXECUCAO DA FUNCAO (OS QUE ESTAO DENTRO)
soma(1, 2, z=5) #se passa um argumento possicional nomeado z=5 todos os proximos
#ou voce chama todos nomeados ou nenhum
#posso passar fora da ordem , posso começar com argumento nao nomeado , porem depois que nomeou todos tem que ser


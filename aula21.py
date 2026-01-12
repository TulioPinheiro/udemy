# Operadores Lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# Verdadeiras.
# Se qualqer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy ( que voce já viu)
#  0 0 0 '' False
# Ta,bém existe o tipo de None que é 
# usado para representar um não valor

entrada = input('[E]ntrar [S]air :')
senha_digitada = input('Senhar: ')

senha_permitida = '123456'
#if True:
# ...
if entrada =='E' and senha_digitada == senha_permitida :
    print('Entrar')
else :
    print('Sair')

#Avaliação de curto circuito
#print (True and False and True) ira para na false nao vai availar os proximos

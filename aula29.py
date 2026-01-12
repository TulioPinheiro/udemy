"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input('vou dobrar o numero que voce digitar :')

try:
    print('Str :', numero_str)
    numero_float= float(numero_str)
    print('Float:', numero_float)
    print(f'o dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('isso não é um numero')

#if numero_str.isdigit():
#tudo abaixo
#else:
#Print('Isso não é um numero)

#numero_float= float(numero_str)
#print(f'o dobro de {numero_str} é {numero_float * 2:.2f}')


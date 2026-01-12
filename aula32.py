"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar .Caso o usuário não digite um número
inteiro, informe que não é um número inteiro
"""
numero = input('Digite um numero :')
try:
    entrada_int = float(numero)
    par_impar = entrada_int % 2 ==0 
    par_impar_texto = 'impar'
    if par_impar :
        par_impar_texto = 'par'
    print(f'O numero {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')


#if numero.isdigit():
#    entrada_int = int(numero)
#    par_impar = entrada_int % 2 ==0 
#    par_impar_texto = 'impar'
#    if par_impar :
#        par_impar_texto = 'par'
#    print(f'O numero {entrada_int} é {par_impar_texto}')
#else:
#    print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e , baseando -se no horário
descrito , exiba a saudação apropriada Ex.
Bom dia 0-11 , Boa Tarde 12-17 e Boa Noite 18-23
"""
entrada = (input('Qual e a hora ? '))
try:
    hora = int(entrada)

    if hora >= 0 and hora<= 11 :
        print(f'Bom dia são {hora} horas')
    elif hora >= 12 and hora  <= 17 :
        print(f'Boa tarde ja são {hora} horas')
    elif hora >=18 and hora <= 23:
        print(f'Boa noite ja são {hora} horas')
    else:
        print('Não conheço essa hora')
except:
    print('por favor , digite um  numero inteiro')


"""
Faça um programa que peça o primeiro nome do usuário . Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto" ; se tiver entre 5 e 6 letras , escreva
"Seu nome é normal " ; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Digite seu nome ?').strip()
letras = len(nome)
if letras > 1:#conferi se tem mais de uma letra
    if letras <= 4 :
        print('Seu nome e curto ')
    elif 5 <= letras <=6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')#pedir pro usuario digitar mais letras
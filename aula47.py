"""
Faça um jogo para o usuarío adivinhar qual
a palavra secreta.
-Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para o usuário digitar apenas letras.
-Qual o usuário digitar uma letra , você 
vai connferir se a letra digitada esta 
na palavra secreta 
    Se a letra digitada estiver na palavra secreta ; 
    exiba a letra ;
    Se a letra digitada não estiver na palavra secreta ; exiba *.
Faça a contagem de tentativas do seu usuário ."""

palavra_secreta = 'galo'
numerode_tentativas = 0
letras_descobertas = ''

while True:
    letra = input('Digite uma letra: ').lower().strip()
    numerode_tentativas += 1

    if len(letra) > 1:
        print('Digite apenas uma letra')
        continue

    if letra in palavra_secreta:
        print(f'✅ A letra "{letra}" existe na palavra!')
        letras_descobertas += letra
    else:
        print(f' A letra "{letra}" não existe.')

    palavra_mostrada = ''
    for l in palavra_secreta:
        if l in letras_descobertas:
            palavra_mostrada += l
        else:
            palavra_mostrada += '*'

    print('Palavra:', palavra_mostrada)

    if palavra_mostrada == palavra_secreta:
        print('Você VENCEU')
        print(f' em {numerode_tentativas} tentativas!')
        numerode_tentativas = 0
        letras_descobertas = '' 
        break

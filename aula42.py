frase = 'O python é uma linguagem de programção ' \
    'multiparadgma. '  \
    'Python foi criado por Guido Van Rossum .'

i = 0
apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''
while i < len (frase) :
    letra_atual = frase [i]

    if letra_atual == ' ' :
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)
    
    if apareceu_mais_vezes < qtd_atual :
        apareceu_mais_vezes = qtd_atual
        letra_que_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi' \
    f'{letra_que_apareceu_mais_vezes}que apareceu '
    f'{letra_que_apareceu_mais_vezes} x'
)
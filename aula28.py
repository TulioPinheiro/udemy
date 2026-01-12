'''
Exercicio
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
se o nome e idade forem digitados :
... Exiba:
    Seu nome é {nome}
    Seu nome invertido é {nome invertido}
    Seu nome contem (ou não) espaços
    Seu nome tem {n} letras
    A primeira Letra do seu nome é {letra}
    A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade :
    exiba " Desculpe , você deixou campos vazios.'''
nome = input('Digite seu nome :').strip()
idade = input('Digite sua idade ').strip()
if nome and idade  :
    print(f'seu nome e {nome}')
    print(f'seu nome invertido é {nome[-1::-1]}')

    if 'n' in nome.lower() :
        print(f'Seu {nome} contem N ')
    else : 
        print(f'seu {nome} não contem N ')
    if ' ' in nome :
        print('Seu nome contém espaço')
    else :
        print('Seu nome não contem espaço')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome e {nome[0]}')
    print(f'A ultima letra do seu nome e {nome[-1]}')
else :
    print('Desculpa nada foi digitado')
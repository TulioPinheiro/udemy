# exercício - sistema de perguntas e respostas

perguntas = [
    {
        'pergunta': 'Qual a capital do Brasil? ',
        'opções': ['São Paulo', 'Rio de Janeiro', 'Brasília', 'Salvador'],
        'resposta': 'Brasília'
    },
    {
        'pergunta': 'Qual o maior planeta do sistema solar? ',
        'opções': ['Terra', 'Júpiter', 'Saturno', 'Vênus'],
        'resposta': 'Júpiter'
    },
    {
        'pergunta': 'Quem pintou a Mona Lisa? ',
        'opções': ['Vincent van Gogh', 'Pablo Picasso', 'Leonardo da Vinci', 'Michelangelo'],
        'resposta': 'Leonardo da Vinci'
    }
]
def fazer_pergunta(pergunta_dict):
    print(pergunta_dict['pergunta'])
    for i, opção in enumerate(pergunta_dict['opções'], start=1):
        print(f"{i}) {opção}")
    resposta_usuario = input("Escolha sua opção: ")
    resposta_correta = pergunta_dict['resposta']
    try:
        resposta_usuario_int = int(resposta_usuario)
        if pergunta_dict['opções'][resposta_usuario_int - 1] == resposta_correta:
            print("Resposta correta!\n")
            return True
        else:
            print(f"Resposta incorreta! A resposta correta é: {resposta_correta}\n")
            return False
    except (ValueError, IndexError):
        print(f"Resposta inválida! A resposta correta é: {resposta_correta}\n")
        return False
def main():
    acertos = 0
    for pergunta in perguntas:
        if fazer_pergunta(pergunta):
            acertos += 1
    print(f"Você acertou {acertos} de {len(perguntas)} perguntas.")
if __name__ == "__main__":
    main()
# vídeo 122 - dicionários - parte 2
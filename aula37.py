""" 
Repetições
While  (enquanto)
Executar uma ação enquanto uma condição for verdadeiro
Loop infinito -> Qunado um código não tem fim
"""
contador = 0

while contador <= 10 :
    contador += 1
    
    if contador == 6:
        print('Não vou mostrar o .6')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break

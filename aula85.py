lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))   #tupla adicionada
lista = [
    (x, y) 
    for x in range (3)
    for y in range (3)
]
lista = [
    [x for y in range(3)]
#   [letra for letra in 'tulio']
#   [(x, letra) for letra in 'tulio']    
    for x in range(3)
]
print(lista)
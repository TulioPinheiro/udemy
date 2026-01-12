"""
 Iterável -> str, range, etc (___iter___)
Iterador - > quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter - > me entregue seu iterador
"""
#exto = iter('Luiz')  #___iter__()

#rint(next(texto))
#print(next(texto))
#print(next(texto))

texto = 'Luiz'  #iterável
iterador = iter(texto) #iterator

while True :
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration :
        break

for letra in texto :
    print(texto)
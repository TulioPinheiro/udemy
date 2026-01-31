# Sets - conjuntos em Python (tipo set)
# Conjuntos são ensinos matemáticos
# Representados graficamente por diagramas de Venn
# Sets em Python são muttáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
#s1 = set('Túlio')
#s1 = {'Túlio', 1, 2, 3}
#print(s1)
s1 = set() # vazio
s1 = {'Túlio', 1, 2, 3} # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - eles não tem índexes ;
# - eles não garantem ordem ;
# - eles são iteráveis ( for, in , not in)
#L1 = [1, 2, 2, 3, 3, 3, 4, 5, 5]
#S1 = set(L1)
#L2 = list(S1)
#print(L2)
#S1 = S1 = {1,2,3, [123]} # ERRO - listas não são imutáveis
#tupla pode ter (123,) pois e mutavel
s1 = {1, 2, 3}
#print(3 in s1)
#for numero in s1:
#   print(numero)

# Métodos úteis :
# add, update, clear, discard, copy, pop,
s1 = set()
s1.add('Túlio')
s1.add(1)
s1.update(('ola mundo', 2, 3, 4)) # iterável
#s1.clear()
s1.discard('ola mundo')
s1.discard('Túlio')
print(s1)

# Operadores úteis :
# união (|), interseção (&), diferença (-), diferença simétrica (^)
# intersecção & (intersection ) Itens presentes em ambos os sets
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ Itens que estão em um ou outro set, mas não em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 - s2
s3 = s1 & s2
s3 = s1 ^ s2
print(s3)
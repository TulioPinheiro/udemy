# Módulo padrão do Python (import, From, as e *)
# https://docs.python.org/3/py-modindex.html
# Inteiro - import nome_modulo
# Vantagens : você tem o namespace do módulo
# Desvantagens: nomes grandes

#import sys

# platform = 'a minha'
# print(sys.platform)
# print (platform)


# Partes- from nome_modulo import objeto1, objeto2
# Vantagens : nomes pequenos
# Desvantagens : Sem o namespace do módulo
# from sys import exit, platform

# print(platform)

# alias 1 - import nome_modulo as apelido
# import sys as s 
# sys =' alguma coisa '
# print(s.platform)

# alias 2 - from nome_modulo import objeto as apelido
# from sys import platform as pf, exit as ex

# print (pf)

# Vantagens : você pode reservar nomes para seu código
# Desvantagens : pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens : import tudo de módulo
# Desvantagens : importa tudo de um módulo
from sys import exit, platform # para importa todos os modulos coloque * depois do import

print(platform)
exit()
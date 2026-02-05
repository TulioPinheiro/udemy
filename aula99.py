#1from sys import path

#1import aula99_package.modulo
#from aula99_package.modulo import modulo

#1from aula99_package.modulo import soma_do_modulo

#1from aula99_package.modulo import *

#print(*path, sep='\n')
#1print(soma_do_modulo(1, 2))
#1print(aula99_package.modulo.soma_do_modulo(1, 2))
#print(modulo.soma_do_modulo(1, 2))
#1print(variavel)
#print(nova_variavel)

#from aula99_package.modulo import soma_do_modulo,fala_oi

#print(__name__)
#1fala_oi()
from aula99_package import soma_do_modulo   

print(aula99_package.soma_do_modulo(2, 3))
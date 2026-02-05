# Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __mais__
# Você pode importa outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __mais__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __mais__ por 
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path 

#try:
#    import sys
#    sys.path.append('C:\Users\Tulio\Desktop')
#except ModuleNotFoundError :
#    ...
#import aula97_m
#import modulo_python
#print('se chama ', __name__)
#print(*sys.path, sep='\n')

import aula97_m
from aula97_m import variavel_modulo, soma

print('este módulo')
print(aula97_m.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(aula97_m.soma(2, 3))
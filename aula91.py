# Introdução ás Generator Functions em Python
# generator = (n for n in range(100))

def generator (n=0, maximum=10):
    while True:
        yield n
        n+= 1

        if n> maximum:
            return
    #yield 1 #pausar
    #return ' Acabou'
    print('Continuando')
    #yield 2 # pausar
    #print('mais uma vez')
    #yield 3 
    #print('vou terminar')
    #return ' Acabou'

gen = generator(n=0)
#print(next(gen))
#print(next(gen))
for n in gen :
    print(n)
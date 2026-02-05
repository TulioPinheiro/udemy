# Try, except, else e finally
# a = 18
# b = 0 
# c = a / b

try :
    a = 18
    b = 0
    #print(b[0])
    print('linha 1'[100])
    c = a / b
    print('linha 2')
except ZeroDivisionError:
    print('Dividiu por zero')
except NameError :
    print('nome b não está definido')
except ( TypeError + IndexError) as error: #melhor dividir em 2 
    print('TyperError, IndexError')
    print('msg', error.__class__.__name__)
except Exception :
    print('Erro Desconhecido.')
    
print('Continuar')
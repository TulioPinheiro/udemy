# dir, hasattr e getattr em Python
string = 'Túlio'
metodo = 'upper'

if hasattr (string, metodo):
    print('existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)
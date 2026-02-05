# try, except, else e finally
try:
    print('Abrir Arquivo')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('dividir zero')
except IndentationError as error:
    print('IndexError')
except (NameError, ImportError):
    print('NameError, ImportError')
else:
    print('nao deu erro')
finally:
    print('fechar arquivo')
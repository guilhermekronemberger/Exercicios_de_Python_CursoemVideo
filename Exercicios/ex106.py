from time import sleep

def escreva(msg):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)


def ajuda(c):
    help(c)


comando = ''
while True:
    escreva('-> SISTEMA DE AJUDA PyHELP <-')
    sleep(0.5)
    comando = (input('Função ou Biblioteca> '))
    if comando.upper() == 'FIM':
        escreva('-> PROGRAMA ENCERRADO! <-')
        break
        
    else:
        ajuda(comando)

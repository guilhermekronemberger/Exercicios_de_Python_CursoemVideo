from pacoteII.interface import *
from time import sleep

while True:
    resposta = menu(['Pessoas cadastradas', 'Novo cadastro', 'Sair'])
    if resposta == 1:
        cabeçalho('Pessoas cadastradas')
    elif resposta == 2:
        cabeçalho('Novo cadastro')
    elif resposta == 3:
        cabeçalho('Encerrando sistema...')
        break
    else:
        print('ERRO! Digite uma opção válida!')
    sleep(1)

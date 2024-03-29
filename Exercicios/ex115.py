from pacoteII.interface import *
from pacoteII.arquivo import *
from time import sleep

arq = 'listagem.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Pessoas cadastradas', 'Novo cadastro', 'Sair'])

    if resposta == 1:
        lerArquivo(arq)

    elif resposta == 2:
        cabeçalho('Novo cadastro')
        nome = str(input('Nome: '))
        idade = leiaint('Idade:')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabeçalho('Encerrando sistema...')
        break
    
    else:
        print('ERRO! Digite uma opção válida!')
    sleep(1)

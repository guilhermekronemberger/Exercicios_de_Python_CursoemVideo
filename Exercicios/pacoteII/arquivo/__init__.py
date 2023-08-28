def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.closed()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.closed()
    except:
        print('ERRO ao criar o arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

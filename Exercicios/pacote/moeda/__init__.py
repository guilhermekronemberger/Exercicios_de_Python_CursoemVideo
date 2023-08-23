def aumentar(valor=0, taxa=0, format=False):
    resposta = valor + (valor * taxa / 100) 
    if format == False:
        return resposta
    else:
        return moeda(resposta)


def diminuir(valor=0, taxa=0, format=False):
    resposta = valor - (valor * taxa / 100)
    if format == False:
        return resposta
    else:
        return moeda(resposta)


def dobro(valor=0, format=False):
    resposta = valor * 2 
    if format == False:
        return resposta
    else:
        return moeda(resposta)


def metade(valor=0, format=False):
    resposta = valor / 2
    if format == False:
        return resposta
    else:
        return moeda(resposta)


def moeda(valor, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')


def resumo(valor=0, taxaaumento=10, taxareduzida=10):
    print('=' * 35)
    print('-> RESUMO DO VALOR <- '.center(35))
    print('=' * 35)
    print(f'Valor analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, format=True)}')
    print(f'Metade do preço: \t{metade(valor, format=True)}')
    print(F'Com {taxaaumento}% de aumento: \t{aumentar(valor, taxaaumento, format=True)}')
    print(F'Com {taxareduzida}% de redução: \t{diminuir(valor, taxareduzida, format=True)}')
    print('=' * 35)

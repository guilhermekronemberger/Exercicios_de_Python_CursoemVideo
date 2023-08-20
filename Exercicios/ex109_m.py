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

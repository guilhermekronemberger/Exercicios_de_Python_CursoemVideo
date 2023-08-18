def aumentar(valor=0, taxa=0):
    resposta = valor + (valor * taxa / 100) 
    return resposta


def diminuir(valor=0, taxa=0):
    resposta = valor - (valor * taxa / 100)
    return resposta


def dobro(valor=0):
    resposta = valor * 2 
    return resposta


def metade(valor=0):
    resposta = valor / 2
    return resposta


def moeda(valor, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')

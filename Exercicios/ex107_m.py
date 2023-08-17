def aumentar(valor, taxa):
    resposta = valor + (valor * taxa / 100) 
    return resposta


def diminuir(valor, taxa):
    resposta = valor - (valor * taxa / 100)
    return resposta


def dobro(valor):
    resposta = valor * 2 
    return resposta


def metade(valor):
    resposta = valor / 2
    return resposta

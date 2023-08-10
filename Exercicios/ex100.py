from random import randint  

def sorteia(lista):
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(0,5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ')
    print()


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, o total é: {soma}.')


numeros = []
sorteia(numeros)
somaPar(numeros)

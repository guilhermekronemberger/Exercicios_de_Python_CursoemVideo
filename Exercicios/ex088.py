from random import randint
from time import sleep

lista = list()
jogos = list()
print('=' * 30)
print(f'{"MEGA SENA":^30}')
print('=' * 30)

quantidade = int(input('Quantos jogos você quer sortear? '))
total = 1

while total <= quantidade:
    contador = 0

    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print(f'{"SORTEANDO..." :^30}')
print('=' * 30)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(0.5)
print(f'{"BOA SORTE!" :^30}')

from random import randint
from time import sleep

print('Tente adivinhar o número que eu estou pensando entre 0 e 5: ')
numero = int(input('Em que número eu pensei? '))

n = randint(0, 5)

print('PROCESSANDO...')
sleep(1)
if n == numero:
    print(f'Você acertou! O número que eu pensei foi o {n}')

else:
    print(f'Você errou! Eu pensei no número {n} e não no {numero}!')
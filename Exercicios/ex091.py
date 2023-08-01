from random import randint
from time import sleep
from operator import itemgetter

dado = { 'Jogador1': randint(1, 6), 'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6), 'Jogador4': randint(1, 6)}

ranking = list()
print('Valores sorteados: ')

for k, v in dado.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
print('=-' * 15)
print(f'RANKING DOS JOGADORES')
print('=-' * 15)
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.5)

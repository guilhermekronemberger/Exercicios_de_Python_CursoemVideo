time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).title()
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()

    for c in range(0, total):
        partidas.append(int(input(f'Quantos gols na partida {c + 1}? ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resposta = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break

        else:
            print('ERRO! Escolha apenas S ou N.')

    if resposta == 'N':
        break

print('=' * 40)
print('Cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print()

print('=' * 40)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()

print('=' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break

    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
        
    else:
        print(f' -> LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'  No jogo {i + 1} faz {g} gols.')
        
    print('-' * 40)
print('>> PROGRAMA ENCERRADO <<')   

from random import randint
from time import sleep

print('SUAS OPÇÕES:\n'
    '[0] Pedra\n'
    '[1] Papel\n'
    '[2] Tesoura\n')

opcoes = ['Pedra', 'Papel', 'Tesoura']
jogador = int(input('Qual sua escolha: '))
computador = randint(0, 2)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')

if computador == 0:
    if jogador == 1:
        print(f'Você escolheu {opcoes[jogador]} e o computador {opcoes[computador]}\n'
              'Você GANHOU!')

    elif jogador == 2:
        print(f'Você escolheu {opcoes[jogador]} e o computador {opcoes[computador]}\n'
              'Você PERDEU!')

    elif jogador == 0:
        print(f'Você escolheu {opcoes[jogador]} e o computador {opcoes[computador]}\n'
              'EMPATE!')
    else:
        print('Opção inválida. Tente novamente!')

elif computador == 1:
    if jogador == 0:
        print(f'Você escolheu {opcoes[jogador]} e o computador {opcoes[computador]}\n'
              'Você PERDEU!')

    elif jogador == 2:
        print(f'Você escolheu {opcoes[jogador]} e o computador {opcoes[computador]}\n'
              'Você GANHOU!')

    elif jogador == 1:
        print(f'Você escolheu {opcoes[jogador]} e o computador {opcoes[computador]}\n'
              'EMPATE!')
    else:
        print('Opção inválida. Tente novamente!')

elif computador == 2:
    if jogador == 0:
        print(f'Você escolheu {opcoes[jogador]} e o computador {opcoes[computador]}\n'
              'Você GANHOU!')

    elif jogador == 1:
        print(f'Você escolheu {opcoes[jogador]} e o computador {opcoes[computador]}\n'
              'Você PERDEU!')

    elif jogador == 2:
        print(f'Você escolheu {opcoes[jogador]} e o computador {opcoes[computador]}\n'
              'EMPATE!')
    else:
        print('Opção inválida. Tente novamente!')

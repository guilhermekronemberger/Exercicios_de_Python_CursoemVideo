from random import randint

print('Vamos jogar PAR ou ÍMPAR')
vitoria = 0

while True:
    valor = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = valor + computador
    resposta = ' '
    
    while resposta not in 'PI':
         resposta = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {valor} e o computador {computador}. Total de {total},', end=' ')
    print('Deu PAR' if total % 2 == 0 else 'Deu ÍMPAR')

    if total % 2 == 0 and 'P' in resposta:
        vitoria += 1
        print('Você venceu!\n'
            'Vamos jogar novamente..')
        
    elif total % 2 != 0 and 'I' in resposta:
        vitoria += 1
        print('Você venceu!\n'
            'Vamos jogar novamente..')
        
    else:
        print('Você perdeu!')
        break

print(f'GAME OVER! Você venceu {vitoria} vezes.')

principal = []
temporario = []
maior = 0
menor = 0

while True:
    temporario.append((str(input('NOME: '))))
    temporario.append((float(input('PESO: '))))
    if len(principal) == 0:
        maior = temporario[1]
        menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]

        elif temporario[1] < menor:
            menor = temporario[1]

    principal.append(temporario[:])
    temporario.clear()

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        break

print(f'Você cadastrou {len(principal)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de', end=' ')
for peso in principal:
    if peso[1] == maior:
        print(f'{[peso[0]]}', end=' ')
print()

print(f'O menor peso foi de {menor}Kg. Peso de', end=' ')
for peso in principal:
    if peso[1] == menor:
        print(f'{[peso[0]]}', end=' ')
print()

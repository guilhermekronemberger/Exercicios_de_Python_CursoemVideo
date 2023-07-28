matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

pares = 0
maiorvalor = 0
somadacoluna = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('=' * 30)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
    print()
    
print('=' * 30)
print(f'A soma dos valores pares é {pares}.')

for linha in range(0, 3):
    somadacoluna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {somadacoluna}.')

for coluna in range(0, 3):
    if coluna == 0:
        maiorvalor = matriz[1][coluna]
    
    elif matriz[1][coluna] > maiorvalor:
        maiorvalor = matriz[1][coluna]

print(f'O maior valor da segunda linha é {maiorvalor}.')

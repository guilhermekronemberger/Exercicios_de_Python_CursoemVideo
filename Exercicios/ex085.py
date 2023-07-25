numeros = [[], []]

for num in range(1, 8):
    valor = int(input(f'Digite o {num}º valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)

    else:
        numeros[1].append(valor)

numeros[0].sort()
numeros[1].sort()

print(f'O valores pares digitados foram: {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')

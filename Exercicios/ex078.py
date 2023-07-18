numeros = []
maior = 0
menor = 0

for contador in range(0, 5):
    numeros.append(int(input(f"Digite o valor para {contador}º posição: ")))
    if contador == 0:
        maior = numeros[contador]
        menor = numeros[contador]

    else:
        if numeros[contador] > maior:
            maior = numeros[contador]

        if numeros[contador] < menor:
            menor = numeros[contador]

print(f'Você digitou os valores {numeros}')

print(f'O MAIOR valor digitador {maior} nas posições: ', end=' ')
for index, valor in enumerate(numeros):
    if valor == maior:
        print(f'{index},', end='')
print()

print(f'O MENOR valor digitador {maior} nas posições: ', end=' ')
for index, valor in enumerate(numeros):
    if valor == menor:
        print(f'{index},', end='')
print()

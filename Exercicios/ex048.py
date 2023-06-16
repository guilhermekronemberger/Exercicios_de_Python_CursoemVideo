contador = 0
soma = 0

for numero in range(1, 501, 2):
    if numero % 3 == 0:
        soma += numero
        contador += 1

print(f'A soma de todos os {contador} valores solicitados são {soma}.')

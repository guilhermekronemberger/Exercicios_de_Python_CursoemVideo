maior_peso = 0
menor_peso = 0

for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: '))

    if p == 1:
        maior_peso = peso
        menor_peso = peso

    else:
        if peso > maior_peso:
            maior_peso = peso

        if peso < menor_peso:
            menor_peso = peso

print(f'O MAIOR peso lido foi de {maior_peso}Kg.\n'
      f'O MENOR peso lido foi de {menor_peso}Kg.')

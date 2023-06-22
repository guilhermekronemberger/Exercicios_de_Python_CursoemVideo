from datetime import date

ano_atual = date.today().year

maior_de_idade = 0
menor_de_idade = 0

for nascimento in range(1, 8):
    nascimento = int(input(f'Em que ano a {nascimento}ª pessoa nasceu: '))
    idade = ano_atual - nascimento

    if idade >= 18:
        maior_de_idade += 1

    else:
        menor_de_idade += 1

print(f'Tivemos {maior_de_idade} pessoas maiores de idade.\n'
      f'Tivemos {menor_de_idade} pessoas menores de idade.')

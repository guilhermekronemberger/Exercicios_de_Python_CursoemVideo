from datetime import date

nascimento = int(input('Ano de Nascimento: '))

ano_atual = date.today().year
idade = ano_atual - nascimento

print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Classificação: Mirim')

elif idade <= 14:
    print('Classificação: Infantil')

elif idade <= 19:
    print('Classificação: Júnior')

elif idade <= 25:
    print('Classificação: Sênior')

else:
    print('Classificação: Master')

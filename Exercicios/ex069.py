total18 = 0
totalmenor20 = 0
totalhomen = 0
totalmulher = 0

while True:
    print('CADASTRO DE PESSOAS')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    
    if idade >= 18:
        total18 += 1

    if sexo == 'M':
        totalhomen += 1

    if idade < 20 and sexo == 'F':
        totalmenor20 += 1
    
    else:
        totalmulher += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        break

print(f'Total de pessoas cadastradas com mais de 18 anos: {total18}')
print(f'Total de homens cadastrados: {totalhomen}')
print(f'Total de mulheres cadastradas com menos de 20 anos: {totalmenor20}')

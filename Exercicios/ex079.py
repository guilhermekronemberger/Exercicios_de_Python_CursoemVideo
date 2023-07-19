numeros = []

while True:
    n = int(input("Digite um valor: "))

    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado!')
        
    else:
        print('O valor já existe nesta lista...')

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        break

numeros.sort()
print(f'Você digitou os valores: {numeros}')

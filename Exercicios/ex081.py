numeros = []

while True:
    numeros.append(int(input('Digite um valor: ')))
    resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        break

print(f'Você digitou {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente são: {numeros}')

if 5 in numeros:
    print('O valor 5 faz parte da lista!')

else:
    print('O valor 5 não foi encontrado na lista!')

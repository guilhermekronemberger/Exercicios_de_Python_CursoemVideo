numeros = []
par = []
impar = []

while True:
    numeros.append(int(input('Digite um valor: ')))
    resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

for i, v in enumerate(numeros):
    if v % 2 == 0:
        par.append(v)

    elif v % 2 == 1:
        impar.append(v)

print(f'A lista completa é: {numeros}\n'
      f'A lista de pares é: {par}\n'
      f'A lista de împares é: {impar}')

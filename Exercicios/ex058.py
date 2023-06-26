from random import randint

print('Gerando um número entre 0 e 10.')
computador = randint(0, 10)
contador = 0

while True:
    numero = int(input('Tente adivinhar o número selecionado: '))

    if numero == computador:
        contador += 1
        print(f'Você acertou com {contador} tentativas. PARABÉNS!')
        break

    else:
        if numero < computador:
            contador += 1
            print('Você ERROU! Tente um número maior..')

        else:
            contador += 1
            print('Você ERROU! Tente um número menor..')

numero = 0
total = 0
contador = 0

numero = int(input('Digite um número [para pausar digite 999]: '))
while numero != 999:
    total += numero
    contador += 1
    numero = int(input('Digite um número [para pausar digite 999]: '))

else:
    print(f'Você digitou {contador} números, e a soma entre eles é {total}.')

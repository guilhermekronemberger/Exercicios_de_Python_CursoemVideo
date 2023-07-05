total = 0
contador = 0

while True:
    numero = int(input('Digite um número [para pausar digite 999]: '))
    if numero == 999:
        break

    else:
        total += numero
        contador += 1
        
print(f'A soma dos {contador} números foi {total}.')

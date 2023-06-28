numero = int(input('Informe o número para calcular seu Fatorial: '))
contador = numero
factorial = 1

while contador > 0:
    if contador > 1:
        print(f'{contador} *', end=' ')

    else:
        print(f'{contador} = ', end=f"{factorial}")
        
    factorial *= contador
    contador -= 1

while True:
    numero = int(input('Deseja ver a tabuada de qual valor? '))

    if numero < 0:
        print('Programa de Tabuada encerrado.')
        break

    else:
        for n in range(1, 11):
            print(f'{numero} x {n} = {numero * n}')

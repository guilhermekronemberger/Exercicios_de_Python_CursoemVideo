def leiaint(msg):
    validador = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            validador = True
        else:
            print('ERRO! Digite um número inteiro válido.')

        if validador:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

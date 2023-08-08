from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1

    if p == 0:
        p = 1

    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)

    if p < 0:
        p *= -1

    if p == 0:
        p = 1

    if i < f:
        c = i 
        while c <= f:
            print(f'{c}', end=' ')
            sleep(0.4)
            c += p
        print('FIM!')

    else:
        c = i
        while c >= f:
            print(f'{c}', end=' ')
            sleep(0.4)
            c -= p
        print('FIM!')
    print('=' * 40)


contador(1, 10, 1)
contador(10, 0, 2)

print('Agora você pode personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)

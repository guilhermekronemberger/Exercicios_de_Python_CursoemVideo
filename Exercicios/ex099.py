from time import sleep

def maior(*args):
    print('=' * 30)
    print('Analisando os valores passados...')
    sleep(0.4)
    maior = 0
    contador = 0
    for n in args:
        print(f'{n}', end=' ')
        sleep(0.3)
        if contador == 0:
            maior = n
            
        else:
            if n > maior:
                maior = n
                
        contador += 1
                
    print(f'Foram informados {contador} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

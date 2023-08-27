def linha(tamanho=40):
    print('=' * tamanho)


def cabeçalho(txt):
    linha()
    print(txt.center(40))
    linha()


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário...')
            return 0
        else:
            return n    


def menu(lista):
    cabeçalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    linha()
    opc = leiaint('Sua opção: ')
    return opc

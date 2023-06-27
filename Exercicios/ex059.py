numero1 = int(input('Informe o primeiro valor: '))
numero2 = int(input('Informe o segundo valor: '))

while True:

    print('[1] SOMAR\n'
          '[2] MULTIPLICAR\n'
          '[3] MAIOR\n'
          '[4] NOVOS NÚMEROS\n'
          '[5] SAIR DO PROGRAMA')
    escolha = int(input('Qual a sua opção: '))

    if escolha == 1:
        print(f'O resultado de {numero1} + {numero2} = {numero1 + numero2}')

    elif escolha == 2:
        print(f'O resultado de {numero1} * {numero2} = {numero1 * numero2}')

    elif escolha == 3:
        if numero1 > numero2:
            print(f'Entre {numero1} e {numero2} o maior é {numero1}')

        else:
            print(f'Entre {numero1} e {numero2} o maior é {numero2}')

    elif escolha == 4:
        print('Informe os números novamente... ')
        numero1 = int(input('Informe o primeiro valor: '))
        numero2 = int(input('Informe o segundo valor: '))

    elif escolha == 5:
        print('Finalizando programa...')
        break

    else:
        print('Opção inválida. Tente novamente..')

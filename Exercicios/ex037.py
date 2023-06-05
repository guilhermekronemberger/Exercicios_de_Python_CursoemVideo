numero = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:\n'
      '[1] converter para BINÁRIO\n'
      '[2] converter para OCTAL\n'
      '[3] converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{numero} convertido para BINÁRIO é igual a {bin(numero)[2:]}')

elif opcao == 2:
    print(f'{numero} convertido para OCTAL é igual a {oct(numero)[2:]}')

elif opcao == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}')

else:
    print('Você precisa digitar uma das opções válidas.')
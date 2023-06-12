print('SISTEMA DE VENDAS')
preco = float(input('valor da compra: R$'))

print('FORMAS DE PAGAMENTO\n'
      '[1] A vista no Dinheiro\n'
      '[2] A vista no Cartão\n'
      '[3] 2x Cartão\n'
      '[4] 3x ou mais no Cartão\n')

opcao = int(input('Escolha uma opção: '))

if opcao == 1:
    total = preco - (preco * 10 / 100)

elif opcao == 2:
    total = preco - (preco * 5 / 100)

elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS.')

elif opcao == 4:
    vezes = int(input('Quantas vezes? '))
    total = preco + (preco * 20 / 100)
    parcela = total / vezes
    print(f'Sua compra será parcelada em {vezes}x de R${parcela:.2f} COM JUROS.')
else:
    print('Opção de pagamento inválida. Tente novamente!')

print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f}.')

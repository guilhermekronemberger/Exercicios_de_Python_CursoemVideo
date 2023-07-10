print('CADASTRO DE PRODUTOS')

total = 0
contador = 0
maiorquemil = 0
menorpreco = 0
produtomaisbarato = ' '

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    contador += 1
    total += preco

    if preco > 1000:
        maiorquemil += 1
    
    if contador == 1 or preco < menorpreco:
        menorpreco = preco
        produtomaisbarato = produto

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        break

print('PROGRAMA ENCERRADO.\n'
    f'O total da sua compra foi de R${total:.2f}\n'
    f'Temos {maiorquemil} produtos custando mais de R$1000\n'
    f'O produto mais barato foi {produtomaisbarato.title()} que custou R${menorpreco:.2f}.')

produto = float(input('Digite o valor do produto: R$'))

desconto = produto - (produto * 5 / 100)

print(f'O produto que custava R${produto}, na promoção com 5% de desconto vai custar R${desconto:.2f}.')
import ex107_m

preco = float(input('Digite o preco: R$'))

print(f'A metade de R${preco} é R${ex107_m.metade(preco)}')
print(f'O dobro de R${preco} é R${ex107_m.dobro(preco)}')
print(f'Aumentando 10%, temos R${ex107_m.aumentar(preco, 10)}')
print(f'Diminuindo 10%, temos R${ex107_m.diminuir(preco, 10)}')

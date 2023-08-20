import ex109_m

preco = float(input('Digite o preco: R$'))

print(f'A metade de {ex109_m.moeda(preco)} é {ex109_m.metade(preco, format=True)}')
print(f'O dobro de {ex109_m.moeda(preco)} é {ex109_m.dobro(preco, format=True)}')
print(f'Aumentando 10%, temos {ex109_m.aumentar(preco, 10, format=True)}')
print(f'Diminuindo 10%, temos {ex109_m.diminuir(preco, 10, format=True)}')

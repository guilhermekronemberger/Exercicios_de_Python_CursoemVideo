import ex108_m

preco = float(input('Digite o preco: R$'))

print(f'A metade de {ex108_m.moeda(preco)} é {ex108_m.moeda(ex108_m.metade(preco))}')
print(f'O dobro de {ex108_m.moeda(preco)} é {ex108_m.moeda(ex108_m.dobro(preco))}')
print(f'Aumentando 10%, temos {ex108_m.moeda(ex108_m.aumentar(preco, 10))}')
print(f'Diminuindo 10%, temos {ex108_m.moeda(ex108_m.diminuir(preco, 10))}')

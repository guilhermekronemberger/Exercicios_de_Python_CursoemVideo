lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90,
         'Estojo', 25, 'Trasferidor', 4.20, 'Compasso', 9.99,
          'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 26)
print(f'{"LISTA DE PREÇOS":^26}')
print('-' * 26)

for x in range(0, len(lista)):
    if x % 2 == 0:
        print(f'{lista[x]:.<15}', end='')
    
    else:
        print(f'R${lista[x]:>7.2f}')

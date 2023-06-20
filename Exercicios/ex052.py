numero = int(input("Digite um número: "))
total = 0

for contador in range(1, numero + 1):
    if numero % contador == 0:
        print(f'({contador})', end=' ')
        total += 1

    else:
        print(contador, end=' ')

print(' ')
print(f'O número {numero} foi divisível {total} vezes')

if total == 2:
    print('É PRIMO!')

else:
    print('NÃO É PRIMO!')

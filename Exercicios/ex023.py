numero = int(input('Informe um número: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f'Analisando o número {numero}\n'
      f'Unidade: {unidade}\n'
       f'Dezena: {dezena}\n'
        f'Centena: {centena}\n'
         f'Milhar: {milhar}')
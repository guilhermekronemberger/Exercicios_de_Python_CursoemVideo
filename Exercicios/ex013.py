salario = float(input('Informe o salário do funcionário: R$'))

novo_salario = salario + ( salario * 15 / 100)

print(f'Um funcionário que ganhava {salario:.2f}, com 15% de aumento, passa a receber {novo_salario:.2f}')
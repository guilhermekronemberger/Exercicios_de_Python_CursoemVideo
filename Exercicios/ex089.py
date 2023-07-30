ficha = []

while True:
    nome = str(input('NOME: ')).title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        break

print('-=' * 15)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-=' * 15)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-=' * 15)

while True:
    escolha = int(input('Mostrar notas de qual aluno? (999 para interromper) '))
    if escolha == 999:
        print('FINALIZANDO...')
        break
        
    if escolha <= len(ficha) - 1:
        print(f'Notas de {ficha[escolha][0]} são {ficha[escolha][1]}')

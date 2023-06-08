nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2

print(f'Tirando {nota1} e {nota2}, a média do aluno é {media:.1f}')

if media >= 7:
    print('Aluno APROVADO!')

elif media < 7 and media >= 5: 
    print('Aluno de RECUPERAÇÃO!')

else:
    print('Aluno REPROVADO!')

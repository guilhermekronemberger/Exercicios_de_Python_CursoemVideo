from datetime import date

nascimento = int(input('Ano de nascimento: '))

ano_atual = date.today().year
idade = ano_atual - nascimento 
idade_alistamento = 18

print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}.')

if idade < idade_alistamento:
   saldo = idade_alistamento - idade
   ano = ano_atual + saldo
   print(f'Ainda faltam {saldo} anos para o alistamento.\n'
         f'Seu alistamento será em {ano}.')

elif idade > idade_alistamento:
   saldo = idade - idade_alistamento 
   ano = ano_atual - saldo
   print(f'Você já deveria ter se alistado há {saldo} anos.\n'
         f'Seu alistamento foi em {ano}.')
   
else:
   print('Você tem que se alistar IMEDIATAMENTE!')

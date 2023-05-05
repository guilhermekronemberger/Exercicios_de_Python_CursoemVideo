valor = input('Digite algo: ')

print(f'O tipo primitivo deste valor é: {type(valor)}')
print(f'Só possui espaços?: {valor.isspace()}')
print(f'É um número?: {valor.isnumeric()}')
print(f'É alfabético?: {valor.isalpha()}')
print(f'É alfanúmerico?: {valor.isalnum()}')
print(f'Ésta em maiúsculas?: {valor.isupper()}')
print(f'Está em minúsculas?: {valor.islower()}')
print(f'Está capitalizada?: {valor.istitle()}')


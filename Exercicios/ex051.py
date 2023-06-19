primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

decimo = primeiro + (10 - 1) * razao

for numero in range(primeiro, decimo + razao, razao):
    print(numero, end=' ')

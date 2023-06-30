primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = primeiro
contador = 1

while contador <= 10:
    print(termo, end=' ')
    termo = termo + razao
    contador += 1

print('Fim')

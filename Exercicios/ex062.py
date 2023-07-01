primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = primeiro
contador = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while contador <= total:
        print(termo, end=', ')
        termo += razao
        contador += 1
    print('pausa')

    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')

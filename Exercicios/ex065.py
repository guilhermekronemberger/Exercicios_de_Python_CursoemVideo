resposta = 'S'
total = 0
contador = 0
maior = 0
menor = 0

while resposta in 'S':
    numero = int(input('Digite um número: '))
    total += numero
    contador += 1

    if contador == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    resposta = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
media = total / contador
print(f'Você digitou {contador} números e a média é {media}.\n'
      f'O maior valor foi {maior} e o menor foi {menor}.')

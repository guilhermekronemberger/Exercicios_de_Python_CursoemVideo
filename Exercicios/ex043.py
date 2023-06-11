peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))

imc = peso / (altura ** 2)

print(f'O IMC dessa pessoa é de {imc:.1f}')

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')

elif imc <= 25:
    print('Você está na faixa de PESO NORMAL')

elif imc <= 30:
    print('Você está em SOBREPESO')
    
elif imc <= 40:
    print('Você está em OBESIDADE, cuidado!')

else:
    print('ATENÇÃO: OBESIDADE MÓRBIDA!')

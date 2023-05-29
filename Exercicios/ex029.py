velocidade_atual = float(input('Qual é a velocidade atual do carro? '))

if velocidade_atual > 80:
    multa = (velocidade_atual - 80) * 7
    print('Você excedeu o limite de velocidade permitido que é de 80km/h. \n'
          f'Você foi MULTADO e deve pagar uma multa de R${multa:.2f}')

print('Tenha um bom dia! Dirija com segurança!')
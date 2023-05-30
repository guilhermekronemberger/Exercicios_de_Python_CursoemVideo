distancia = float(input('Qual é a distância da sua viagem? '))

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print(f'Você fará uma viagem de {distancia}KM.\n'
      f'E o preço da sua passagem será de R${preco:.2f}')      
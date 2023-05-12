largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))

area = largura * altura
litro = area / 2

print(f'Sua parede tem a dimensão de {largura}x{altura}, e sua área é de: {area}m². \n'
      f'Para pintar sua parede, você vai precisar de: {litro}L de tinta.')

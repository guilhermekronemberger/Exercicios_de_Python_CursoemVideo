medida = float(input('Informe uma distância em metros: '))

dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida / 1000

print(f'A medida de {medida} metros, corresponde a:\n'
      f'{km} quilômetros, {hm} hectômetros, {dam} decâmetros, \n'
      f'{dm} decímetros, {cm} centímetros, {mm} milímetros')

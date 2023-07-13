times = ('Botafogo', 'Flamengo', 'Grêmio', 'Fluminense', 'Palmeiras', 'Bragantino',
        'Fortaleza', 'São Paulo', 'Cruzeiro', 'Internacional', 'Athletico-PR', 'Atlético-MG',
        'Santos', 'Cuiabá', 'Corinthians', 'Bahia', 'Goiás', 'Coritiba', 'Vasco da Gama', 'América-MG' )

print('=' * 50)
print(f'Lista de times do Brasileirão: {times}')
print('=' * 50)
print(f'Os 5 primeiros são : {times[0:5]}')
print('=' * 50)
print(f'Os 5 ultimos são : {times[-4:]}')
print('=' * 50)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=' * 50)
print(f'O Botafogo está na {times.index("Botafogo") + 1}º posição')

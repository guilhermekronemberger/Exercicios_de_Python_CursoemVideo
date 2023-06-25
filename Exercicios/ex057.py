while True:
    sexo = str(input('Informe seu sexo M/F: ')).upper()[0]

    if 'M' in sexo or 'F' in sexo:
        print(f'Sexo {sexo} registrado com sucesso!')
        break

    else:
        print('Dados inválidos! Tente novamente...')

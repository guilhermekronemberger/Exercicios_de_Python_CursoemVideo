nome = input('Digite seu nome completo: ').strip()

separa = nome.split()

print(f'Seu nome em maiúsculas é: {nome.upper()}\n'
      f'Seu nome em minúsculas é: {nome.lower()}\n'
      f'Seu nome completo possui: {len(nome) - nome.count(" ")} Letras\n'
      f'Seu primeiro nome é: {separa[0].title()}, e possui {len(separa[0])} Letras\n')
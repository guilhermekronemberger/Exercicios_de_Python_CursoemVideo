nome = input('Digite seu nome completo: ').strip().title()

nome = nome.split()

print(f'Prazer em lhe conhecer!\n'
      f'Seu primeiro nome é {nome[0]} e seu último {nome[-1]}.')
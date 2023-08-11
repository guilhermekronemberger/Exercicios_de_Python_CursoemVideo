def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano

    if idade < 16:
        return f'Com {idade} anos: Não vota!'
    elif idade >= 16 and idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto opcional!'
    else:
        return f'Com {idade} anos: Voto obrigatório!'


nascimento = int(input('Digite o ano em que você nasceu: '))    
print(voto(nascimento))

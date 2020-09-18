def voto(ano):
    from  datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Nao Vota.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto Opcional'
    else:
        return f'Com {idade} anos: Voto Obrigatório.'

#programma principal
nasc = int(input('Em que ano voce nasceu'))
print(voto(nasc))

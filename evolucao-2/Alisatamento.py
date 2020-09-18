from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} anos em {}.'.format(nasc,idade,atual))
if idade ==18:
    print('Voce tem que ser alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para ser alista'.format(saldo))
    ano = atual + idade
    print(' seu alistamento foi em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce ja deveria ter ser alistado ha {} anos.'.format(saldo))
    ano = atual - saldo
    print(' seu alistamento foi em {}'.format(ano))
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos. '.format(idade))
if idade <= 9:
    print('Classificado:Mirim')
elif idade <= 14:
    print('Classificado:Infatil')
if idade <= 19:
    print('Classificado:Junior')
if idade <= 25:
    print('Classificado:Sênio')
else:
    print('Classificado:Master')
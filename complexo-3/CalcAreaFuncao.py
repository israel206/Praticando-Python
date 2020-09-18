def area(larg,comp):
    a = larg * comp
    print(f'A area de um terrenno {larg} x {comp} é de {a}m²')

#PROGRAMA PRINCIPAL
print('Controle de Terreno')
print('-'*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)
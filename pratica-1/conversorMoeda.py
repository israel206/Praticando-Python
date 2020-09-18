real = float(input('Quanto dinheiro voce tem na carteira? R$ '))
dolar = real / 3.97
print('Com R${:.2f} voce pode comprar US${:.2f}'.format(real,dolar))
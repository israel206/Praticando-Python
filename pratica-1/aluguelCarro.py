dias = int(input('Quantos dias alugados? '))
Km = float(input('Quanto Km rodado? '))
pago = (dias * 60) + (Km * 0.15)
print('O total a pagar é R${:.2f}'.format(pago))
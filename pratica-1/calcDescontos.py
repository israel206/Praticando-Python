preco = float(input('Qual é o preco do produto? R$'))
novo = preco - (preco * 5 / 100)
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${}'.format(preco, novo))
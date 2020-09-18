distancia = float(input('Qual e a distancia da sua viagem? '))
print('Voce esta prestes a comecar uma viagem de {}km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
'''preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45 manena simplificada'''
print('E o preco de sua viagem será de R${:.2f}'.format(preco))
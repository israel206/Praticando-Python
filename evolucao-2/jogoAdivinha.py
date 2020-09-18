from random import randint
from time import sleep
computador = randint(0,5)#Faz o cpmputador 'PENSAR'
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))#Jogador tenta adivinhar
print('processando...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você me ganhou!')
else:
    print('GANHEI! Eu pensei no numéro {} e não no {}!'.format(computador,jogador))
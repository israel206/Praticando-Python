from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)
print('''Suas opçoes:
[0] pedra
[2]papel
[3] tesoura''')
jogador = int(input('Qual é sua jogada? '))
print('JOO!!!')
sleep(1)
print('KENN!!!')
sleep(1)
print('POO!!!')
print('-='*12)
print('Cmputador jogou {}'.format(itens[computador]))
print('Jogador jogou'.format(itens[jogador]))
print('-='*12)
if computador == 0:# computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('Opcão invalida!')

elif computador == 1:# computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('jogador venceu')
    else:
        print('Opcão invalida!')

elif computador == 2:# computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Opcão invalida!')

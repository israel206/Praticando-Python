from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor; '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impa? [P/I] ')).strip().upper()[0]
    print(f'voce jogou{jogador} e o computador {computador}. total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce venceu!')
            v += 1
        else:
            print('Voce Perdeu!')
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce venceu!')
            v += 1
        else:
            print('Voce Perdeu')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Voce venceu {v} vezes.')

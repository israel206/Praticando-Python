listagem = []
mai = 0
men = 0
for c in range(0,9):
    listagem.append(int(input(f'Digite um valor para a Posiçao {c}: ')))
    if c == 0:
        mai = men = listagem[c]
    else:
        if listagem[c]>mai:
            mai = listagem[c]
        if listagem[c]<men:
            men = listagem[c]
print('=-'*30)
print(f'voce digitou os valores {listagem}')
print(f'O maior valor digitado foi{mai} nas posicoes', end='')
for i, v in enumerate(listagem):
    if v == mai:
        print(f'{i}... ', end='')
    print()
print(f'O menor valor digitado foi {men} nas posicoes', end='')
for i, v in enumerate(listagem):
    if v == men:
        print(f'{i}... ', end='')
    print()

temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append((temp[:]))
    temp.clear()
    resp = str(input('Que continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Os dados foram {princ}')
print(f'Ao todos,voce cadastrou {len(princ)} pessoas.')

print(f'O maior peso foi de {maior}kg. peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso foi de {menor}kg.')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}', end='')
print()
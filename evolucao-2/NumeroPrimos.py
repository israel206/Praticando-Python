num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('\n\033[mO nnumero {} foi divisel {} vezes'. format(num, tot))
if tot == 2:
    print(' é por isso ele é PRIMO')
else:
    print('é por isso nao PRIMO')
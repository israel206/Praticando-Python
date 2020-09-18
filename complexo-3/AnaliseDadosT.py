num = (int(input('Digite um numeros:')),
       int(input('Digite outro numeros:')),
       int(input('Digite mais um numeros:')),
       int(input('Digite o ultimo numeros:')))
print(f'Voce digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posicao')
else:
    print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

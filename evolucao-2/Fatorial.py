from math import factorial
n = int(input('Digite um numero para calcular seu fatorial: '))
f = factorial(n)
print('O Fatorial de {} é {}.'.format(n,f))

# metodos tradicional
n = int(input('Digite um numero para calcular seu fatorial: '))
c = 0
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{} x '.format(c), end='')
    print(' x ' if c > 1 else '=', end='')
    f *= c
    c -= 1
print('{}'.format(f))



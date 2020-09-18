n = int(input('digite o numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O doblo de {} vale{}'.format(n,d))
print('O triplo de {} vale{}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n,t,n,r))

m = int(input('digite o numero: '))
print('O doblo de {} vale{}'.format(n,(n * 2)))
print('O triplo de {} vale{}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n,(n * 3),n,(n **(1/2))))
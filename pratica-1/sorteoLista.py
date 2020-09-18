'''import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('tercero aluno: '))
n4 = str(input('quarto aluno: '))
lista = [n1,n2,n3,n4]
escolhida = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhida))'''

from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('tercero aluno: '))
n4 = str(input('quarto aluno: '))
lista = [n1,n2,n3,n4]
escolhida = choice(lista)
print('O aluno escolhido foi {}'.format(escolhida))
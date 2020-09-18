frase = str(input('digite uma frase: ')).upper().strip()
print('A letra A aparecer {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A aparecer na posiçao {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
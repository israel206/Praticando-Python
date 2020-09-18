frase = str(input('digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]#forma simplificada
'''for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]'''
print('inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo')
else:
    print('a frase digitada nao e um palindromo')
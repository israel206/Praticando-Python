cont = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')
while True:
    num = int(input('Digite um numero entre 0 e 10: '))
    if 0 <= num <= 10:
        break
    print('Tente novamente.', end='')
print(f'Voce digitou o numero {cont[num]}')# utilizando f String formatação
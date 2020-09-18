casa = float(input('Valor da casa:R$'))
salario = float(input('salario do compardor: R$'))
anos = int(input('quantos anos finaciando? '))
prestacao = casa/(anos*12)
minimo = salario * 30/100
print('para pagar uma casa de {:.2f} em {} anos'.format(casa,anos), end='')
print('a prestacao sera de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser Concedido!')
else:
    print('Emprestimo Negado!')
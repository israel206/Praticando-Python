print('{:=^40}'.format('LOJA DE ISRAEL '))
preco = float(input('Preços das compras: R$'))
print('''FORMAS DE PAGAMENTOS
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opçao? '))
if opcao == 1:
    total = preco - (preco * 10/100)
elif opcao == 2:
    total = preco - (preco * 5/100)
elif opcao == 3:
    total = preco
    parcela = total/2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco *20 / 100)
    totalparc = int(input('Quantas parcela? '))
    parcela = total/totalparc
    print('Sua compra sera parcela em {}x de R${}:.2f COM JUROS'.format(totalparc,parcela))
else:
    total = 0
    print('OPÇAO INVALIDA de pagamentos. tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} nno final.'.format(preco,total))

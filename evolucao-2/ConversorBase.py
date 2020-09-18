num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversçao;
[1] converter para BINARIO
[2]converter para OCTAL
[3] converter para HEXADECIAML''')
opcao = int(input('Sua opcao: '))
if opcao == 1:
    print('{} convertendo para BINARIO é igual a {}'.format(num,bin()[2:]))
elif opcao == 2:
    print('{} convertendo para OCTAL é igual a {}'.format(num,oct()[2:]))
elif opcao == 3:
    print('{} convertendo para HEXADECIAML é igual a {}'.format(num,hex()[2:]))
else:
    print('Opcao invalida. Tente novamente.')
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] Somar
    [2]Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do Programa''')
    opcao = str(input('Qual é a sua opcao? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} é {}'.format(n1,n2,soma))
    elif opcao == 2:
        produto = n1 * n2
        print(' O resultado de {} x {} é {}'.format(n1,n2,produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1,n2,maior))
    elif opcao == 4:
        print('Informe os numeros novamentes')
        n1 = int(input('primeiro: '))
        n2 = int(input('Segundo: '))
    elif opcao == 5:
        print('Finalizando..')
    else:
        print('Opcao invalida. tente novamente')
    print('=-=' * 10)
print('Fim do programa')
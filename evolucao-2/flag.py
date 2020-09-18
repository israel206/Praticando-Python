soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para): '))
    if num == 999:
        break
    cont +=1
    soma += num
print('A soma dos {cont} valores foi {soma}!')
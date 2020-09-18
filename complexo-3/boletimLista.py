ficha = list() #variavel composta
while True:#loop infinito
    nome = str(input('Nome; '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    nota3 = float(input('Nota3: '))
    media = (nota1 + nota2 + nota3)/3
    ficha.append(([nome,nota1,nota2,nota3],media))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-='*30)
print(ficha)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')#caractere alinha a esquerda:<4,:<10,:>8 a direita
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{[2]:>8.1f}')
while True:
    print('-=' * 35)
    opc = int(input('Mostra notas de qual aluno?(999 interrompe: '))
    if opc == 999:
        print('FINALIZA...')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} sao {[ficha][1]}')
print('<<<VOLTE SEMPRE>>>')

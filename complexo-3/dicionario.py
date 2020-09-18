aluno = dict() #{} ou com dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['Media'] >= 7:
    aluno['situaçaõ'] = 'Aprovado'
elif 5 <= aluno['Media'] < 7:
    aluno['situaçaõ'] ='Recuperação'
else:
    aluno['situaçaõ'] = 'Reprovação'
print('-='*30)
for k,c in aluno.items():
    print(f' - {k} é igual a {v}')
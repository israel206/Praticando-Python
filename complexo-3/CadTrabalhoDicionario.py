from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados ['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contrataçao: '))
    dados['salario'] = float(input('Salario: R$'))
    dados ['aposentadoria'] = dados['idade'] + ((dados['contratação']+ 35) - datetime.now().year)
print('-='*30)
for k,v in dados.items():# deixando mais bonitos os dados
    print(f'  - {k} tem o valor {v}')
    
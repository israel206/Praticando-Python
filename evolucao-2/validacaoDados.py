sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('dados invalidos. Po favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registro com sucesso'.format(sexo))
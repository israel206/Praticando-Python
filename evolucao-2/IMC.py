peso = float(input('qual é seu peso? (kg) '))
altura = float(input('qual é sua altura? (m) '))
imc = peso/(altura **2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta ABAIXO DO PESO normal')
elif 18.5 <= imc < 30:
    print('Parabéns voce esta na faixa de peso normal')
elif 25 <= imc < 30:
    print('Voce esta em sobrepeso')
elif 30 <= imc < 40:
    print(' voce esta em odesidade!')
elif imc >= 40:
    print('voce esta em obesidade Mórbida, cuidaddo!')
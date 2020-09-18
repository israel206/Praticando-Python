def resposta():
    #Capturando a resposta do usurario e o preprocessamento-a
    resp = input('>: ')
    resp = resp.lower()
    resp = resp.replace('é','eh')
    return resp

def pegaNome(nome):
    if 'O meu nome eh ' in nome:
        nome = nome[14:]

    nome = nome.title()
    return nome

def respondeNome(nome):
    pessoas = ['Charlles', 'Israel','Carlos']

    if nome in pessoas: # variavel pessoa, do object pessoas
        frase = 'Eaew '
    else:
        frase = 'Muito prazer '

    return frase+nome
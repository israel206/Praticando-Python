import json
class aChatBot():
    def __init__(self, nome):
        try:
            memoria = open(nome+'.json','r')
        except FileNotFoundError:
            memoria = (nome+'.json','w')
            memoria.write('["israel"]')
            memoria.close()
            memoria = open(nome+'.json','r')
        self.nome = nome
        self.pessoas = json.load(memoria)
        memoria.close()
        self.historico = []


    def escuta(self):
        frase = input('>: ')
        frase = frase.lower()
        frase = frase.replace('é','eh')
        return frase

    def pensa(self,frase):
        self.frase = {'oi', 'Ola, qual é seu nome?','tchau:','tchau'}

        if frase == 'aprende':
            chave = input('Digite a frase: ')
            resp = input('Digite a resposta: ')
            self.frases[chave] = resp
            return 'Aprendindo'
        if frase in self.frases:
            return self.frases[frase]

        if self.historico[-1] == 'ola, qual é o seu nome?':
            nome = self.pegaNome(frase)
            frase = self.respondeNome(nome)
            return frase

        return 'Não entendi'

    def pegaNome(self,nome):
        if 'O meu nome eh ' in nome:
            nome = nome[14:]

        nome = nome.title()
        return nome

    def respondeNome(self,nome):

        if nome in self.pessoas:  # variavel pessoa, do object pessoas
            frase = 'Eaew '
        else:
            frase = 'Muito prazer '
            self.pessoas.append(nome)
            memoria = open(self.nome+'.json','w')
            json.dump(self.pessoas,memoria)
            memoria.close()
        return frase + nome

    def fala(self,frase):
        print(frase)
        self.historico.append(frase)

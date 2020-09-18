from aChatBot import aChatBot

Bot = aChatBot("test")
while True:
    frase = Bot.escuta()
    resp = Bot.pensa(frase)
    Bot.fala(resp)
    if resp == 'tchau':
        break
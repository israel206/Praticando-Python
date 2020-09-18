# parte do chat bot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

# speech recongnition
import speech_recognition as sr

# speech synthesis
import pyttsx3

bot = ChatBot ('test')# inicia o bot

speak = pyttsx3.init('sapi5')

def Speak(text):
    speak.say(text)
    speak.runAndWait()

conversa = ['Oi', 'Olá', 'Tudo bem?', 'Eu estou bem', 'qual é seu nome?', 'meu nome é']# conversas

bot.set_trainer(ListTrainer) #definir o metodos de treinamentos
bot.train(conversa) # definir a listas de conversas

r = sr.Recognizer()
with sr.Microphone as s:
    r.adjust_for_ambient_noise(s) # se adaptar ao ruído
    print('diga algo!')

    while True:
        try:
            audio = r.listen(s) # escutar

            speech = r.recognize_google(audio) #fala

            response = bot.get_response(speech)

            print('Você: ', speech)
            print('Bot: ', response)
            Speak(response)
        except:
            print('Eu não sei!')





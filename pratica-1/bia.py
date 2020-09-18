import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print('diga algo')
    audio = r.listen(source)

try:
    print('Voce disse:' + r.recognize_google(audio, language='pt-BR'))
except sr.UnknownValueError:
    print('Bia nao pode entender o audio')
except sr.RequestError as e:
    print('Erro ao chama Google Speech Recognition service;{0}',format(e))
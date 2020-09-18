'''import pygame
pygame.init()
pygame.mixer.music.load('ex01.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''

from pygame import mixer
mixer.init()
mixer.music.load('ex01.mp3')
mixer.music.play()
input('Agora você escuta?')
from funcaomultiplayer import *
from threading import Thread

import pygame

def rodarJogo():
    bemVindos()
    definirJogadores()
    inicioJogo()

def tocarJingle():
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load("JingleBells.mp3")
    pygame.mixer.music.play()
    pygame.event.wait()

Thread(target=rodarJogo).start()
Thread(target=tocarJingle).start()
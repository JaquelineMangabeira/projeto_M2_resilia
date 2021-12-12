from funcaomultiplayer import *

def rodarJogo():
    bemVindos()
    definirJogadores()
    inicioJogo()

Thread(target=tocarJingle).start()
Thread(target=rodarJogo).start()
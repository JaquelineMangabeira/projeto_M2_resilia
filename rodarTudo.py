from funcaomultiplayer import *

def rodarJogo():
    bemVindos()
    definirJogadores()
    inicioJogo()
    imprimePodio()

Thread(target=tocarJingle).start()
Thread(target=rodarJogo).start()
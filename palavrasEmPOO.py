import random

marcador = ' __ '

class Palavra():
    
    palavra = ''
    letrasEscondidas = ''
    
    def setPalavra(self, listaPalavras):
        self.palavra = random.choice(listaPalavras).upper()

    def getPalavra(self):
        return self.palavra

    def setLetrasEscondidas(self, palavra):
        esconder = palavra
        verificaLetras = []
        for i in esconder:
            if i.isspace():
                verificaLetras.append(('     '))
            else:
                verificaLetras.append(marcador)
        self.letrasEscondidas = verificaLetras 
    
    def getLetrasEscondidas(self):
        return self.letrasEscondidas






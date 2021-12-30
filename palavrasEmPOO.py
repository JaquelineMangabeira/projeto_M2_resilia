import random
class Palavra():
    
    palavra = ''
    letrasEscondidas = ''
    
    def setPalavra(self, listaPalavras):
        self.palavra = random.choice(listaPalavras).upper()

    def getPalavra(self):
        return self.palavra

    def setLetrasEscondidas(self, palavra):
        self.letrasEscondidas = ['       ' if i.isspace() else ' __ ' for i in palavra]
    
    def getLetrasEscondidas(self):
        return self.letrasEscondidas
import random

marcador = ' __ '

listaPalavras = ["boneco de neve", "papai noel", "treno", "sinos", "estrela de belem", "presepio", "pinheiro",
    "guirlanda", "advento", "panetone", "ceia", "tres reis magos", "uvas passas", "pave ou pra comer", "chamine",
    "luzes de natal", "presentes", "carta", "bolas de natal", "feliz natal", "arvore de natal"] 

class Palavra():
    palavra = ''
    letrasEscondidas = ''
    
    def getPalavra(self):
        self.palavra = random.choice(listaPalavras).upper()
        return self.palavra
    
    def getLetrasEscondidas(self):
        esconder = self.palavra
        verificaLetras = []
        for i in esconder:
            if i.isspace():
                verificaLetras.append(('     '))
            else:
                verificaLetras.append(marcador)
        return verificaLetras


objCarro = Palavra()
print(objCarro.getPalavra())
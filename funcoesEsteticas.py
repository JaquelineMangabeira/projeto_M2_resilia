cEnd = '\033[0m'
bInv = '\033[;7m'

def titulos(msg, cor):         #função de formatação
    print()
    print(bInv + cor + msg.center(100) + cEnd)
    print()


def colorir(msg, cor = '\033[31m'):                      #função de formatação
    print(cor + ('=' * 100) + cEnd)
    print(cor + msg.center(100)+ cEnd)
    print(cor + ('=' * 100) + cEnd)
def titulos(msg, cor):         #função de formatação
    bInv = '\033[;7m'
    cEnd = '\033[0m'
    print()
    print(bInv + cor + msg.center(100) + cEnd)
    print()


def passouDeFase(msg):            #função de formatação
    cEnd = '\033[0m'
    cGre = '\033[32m'
    print(cGre + ('=' * 100) + cEnd)
    print(cGre + msg.center(100)+ cEnd)
    print(cGre + ('=' * 100) + cEnd)


def perdeu(msg):                      #função de formatação
    cEnd = '\033[0m'
    cRed = '\033[31m'
    print(cRed + ('=' * 100) + cEnd)
    print(cRed + msg.center(100)+ cEnd)
    print(cRed + ('=' * 100) + cEnd)
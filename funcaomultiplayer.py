import random
from time import sleep
from funcoesEsteticas import *
from menusNavegacao import *
import re

jogadores = []
podio = [[], []]   #indice 0 - ganhadores - indice 1 perdedores
marcador = ' __ '
vez = 0  # a vez é o indice da lista de cada jogador
cores = ['\033[1;31m','\033[1;41m','\033[1;32m','\033[1;42m','\033[1;33m','\033[1;34m','\033[1;44m','\033[1;35m',
    '\033[1;45m','\033[1;36m','\033[1;46m','\033[1;37m','\033[1;90m','\033[1;100m','\033[1;91m','\033[1;101m',
    '\033[1;92m','\033[1;102m','\033[1;93m','\033[1;94m','\033[1;104m','\033[1;95m','\033[1;105m',
    '\033[1;96m']#tirar as cores ilegíveis, precisa testar

listaPalavras = ["boneco de neve", "papai noel", "treno", "sinos", "estrela de belem", "presepio", "pinheiro",
    "guirlanda", "advento", "panetone", "ceia", "tres reis magos", "uvas passas", "pave ou pra comer", "chamine",
    "luzes de natal,", "presentes", "carta", "bolas de natal", "feliz natal", "arvore de natal"] 

def palavraSecreta():          # sortear palavras secretas
    palavra_secreta = random.choice(listaPalavras).upper() #a palavra secreta é sorteada da lista                                                  
    return palavra_secreta


def letrasAcertadas(palavra):         # função para mostrar as letras de forma legivel
    verificaLetras = []
    for i in palavra:
        if i.isspace():
            verificaLetras.append(('     '))
        else:
            verificaLetras.append(marcador)
      
    return verificaLetras

def InputNumeroDeJogadores():
    while(True):
        try:
            numeroJogadores = int(input('Quantas pessoas irão jogar? '))
        except ValueError:
            print("Valor inválido inserido! Por favor digite um número inteiro")
            continue
        if numeroJogadores > 20:
            print('Limite de jogadores atingido. Max 20 jogadores')
            continue
        return numeroJogadores


def definirJogadores():      # define quantos jogadores irão jogar e atribui a cada um deles - uma palavra, a qttd de erros e uma cor
    print()
    
    numeroJogadores = InputNumeroDeJogadores()
    for i in range(numeroJogadores):                #dando os nomes de cada jogador 
        nome = input(f'Informe o jogador {i+1}: ')
        
        jogadores.append({'nome':nome, 'erros': 0})     #cria um dict e add a chave erros
        jogadores[i].update(palavra = palavraSecreta())   #adiciona a palavra secreta ao dict
        jogadores[i].update(letrasAcertadas = letrasAcertadas(jogadores[i]['palavra']))  #adiciona as letras acertadas ao dict
        
        cor = random.choice(cores)   #soteia uma cor por jogador
        jogadores[i].update(cor = cor)               #adiciona a cor ao dict
        cores.remove(cor) #para não repetir as cores
        
    return jogadores


def rodarJogadores():           # para rodar os jogadores caso perde ou ganha
    global vez
    if vez > len(jogadores) - 1: #se o indice chega ao fim
        vez = 0                     #volta ao primeiro jogador (indice 0)

    titulos(f'Vez do jogador {jogadores[vez]["nome"]}', jogadores[vez]['cor'])
    print(f'Restam {6 - jogadores[vez]["erros"]} tentativas')
    print(jogadores[vez]['letrasAcertadas'])


def tentativa():
    while(True):
        chute = input('\nQual letra? ').strip().upper()
        confirmar = input(
            "\n Confirma? \n Pressione 'n' e depois enter para cancelar, ou apenas enter para prosseguir.\n"
            )
        if confirmar != 'n':
            if len(chute) != 1:
                print("Por favor, digite apenas uma letra por vez.")
            # verifica se a letra pertence ao alfabeto
            elif re.match("[A-Za-z]", chute) is None:
                print(f"{chute} é um caracter inválido, tente novamente!")
                continue
            break
        else:
            continue
          
    return chute

def imprimePodio():

    if len(podio[0]) == 0:
        print('Não houveram ganhadores')
    else:
        colocacao = 1
        for i in podio[0]:
            print(f'{colocacao}º lugar', end= ' - ')
            print(i)
            colocacao += 1

def acertouLetra(tentativa):    
        index = 0
        if tentativa in jogadores[vez]['letrasAcertadas']:
            print('Letra já informada, escolha outra')

        for letra in jogadores[vez]['palavra']:
            if (tentativa.upper() == letra.upper()):
                jogadores[vez]['letrasAcertadas'][index] = letra                
            index += 1
        print(f'Bela tentativa, adicionando letra {tentativa}')
        print(jogadores[vez]['letrasAcertadas'])
            
        if marcador not in jogadores[vez]['letrasAcertadas']:
            ganhador = jogadores[vez]['nome']
            passouDeFase(f'{ganhador} acertou a palavra')
            podio[0].append(jogadores[vez]['nome'])                     #adiciona o nome ao pódio
            jogadores.remove(jogadores[vez])                        #remove vencedor da lista de jogadores
            if len(jogadores) > 0:
                rodarJogadores()
            else:
                imprimePodio()


def errouLetra():
    global vez
    jogadores[vez]['erros'] += 1
    desenha_forca(jogadores[vez]['erros'])
    
    if jogadores[vez]['erros'] == 6:
        perdeu(f'{jogadores[vez]["nome"]} foi enforcado. A palavra era {jogadores[vez]["palavra"] }')          
        
        podio[1].append(jogadores[vez]['nome'])  #adiciona o nome ao pódio
        jogadores.remove(jogadores[vez]) #remove perdedor da lista de jogadores
        
        if len(jogadores) == 0:
            perdeu('Fim de Jogo')
            imprimePodio()
        else:
            rodarJogadores()
    
    else:
        vez += 1
        perdeu('Passou a vez')
        rodarJogadores()


def desenha_forca(erros):
    print("  _______     ")
    sleep(0.1)
    print(" |/      |    ")
    sleep(0.1)

    if(jogadores[vez]['erros'] == 1):
        print(" |      (_)   ")
        sleep(0.1)
        print(" |            ")
        sleep(0.1)
        print(" |            ")
        sleep(0.1)
        print(" |            ")

    if(jogadores[vez]['erros'] == 2):
        print(" |      (_)   ")
        sleep(0.1)
        print(" |      \|    ")
        sleep(0.1)
        print(" |            ")
        sleep(0.1)
        print(" |            ")

    if(jogadores[vez]['erros'] == 3):
        print(" |      (_)   ")
        sleep(0.1)
        print(" |      \|/   ")
        sleep(0.1)
        print(" |            ")
        sleep(0.1)
        print(" |            ")

    if(jogadores[vez]['erros'] == 4):
        print(" |      (_)   ")
        sleep(0.1)
        print(" |      \|/   ")
        sleep(0.1)
        print(" |       |    ")
        sleep(0.1)
        print(" |            ")

    if(jogadores[vez]['erros'] == 5):
        print(" |      (_)   ")
        sleep(0.1)
        print(" |      \|/   ")
        sleep(0.1)
        print(" |       |    ")
        sleep(0.1)
        print(" |      /     ")

    if (jogadores[vez]['erros'] == 6):
        print(" |      (_)   ")
        sleep(0.1)
        print(" |      \|/   ")
        sleep(0.1)
        print(" |       |    ")
        sleep(0.1)
        print(" |      / \   ")


def inicioJogo(): # iniciar o jogo
    global vez
    
    rodarJogadores() 
    
    while len(jogadores) > 0:
        
        chute = str(tentativa())
        if chute in jogadores[vez]['palavra']:
            acertouLetra(chute)
                
        else:
            errouLetra()

    return podio

def rodarJogo():
    bemVindos()
    definirJogadores()
    inicioJogo()

rodarJogo()
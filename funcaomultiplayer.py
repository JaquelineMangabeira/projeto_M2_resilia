from random import randint
from time import sleep
from funcoesEsteticas import *
from menuP import *
from palavrasEmPOO import *
import re
from desenhoForca import desenha_forca

######################### CREATE LIST FOR MODULE STATISTICS
import statistics as s
aux_list = list()
control_list = list()
jgReinicio = list()
######################### MODULESTATISTIC


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
    "luzes de natal", "presentes", "carta", "bolas de natal", "feliz natal", "arvore de natal"] 


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
    global jgReinicio
    print()

    numeroJogadores = InputNumeroDeJogadores()

    for i in range(numeroJogadores):                #dando os nomes de cada jogador 
        nome = input(f'Informe o jogador {i+1}: ')
        
        sorteio = Palavra()
        jogadores.append({'nome':nome, 'erros': 0})     #cria um dict e add a chave erros
        sorteio.setPalavra(listaPalavras)
        palavraSorteada = sorteio.getPalavra()
        jogadores[i].update(palavra = palavraSorteada)   #adiciona a palavra secreta ao dict
        sorteio.setLetrasEscondidas(palavraSorteada)
        letrasAcertadas = sorteio.getLetrasEscondidas()
        jogadores[i].update(letrasAcertadas = letrasAcertadas)  #adiciona as letras acertadas ao dict
        
        cor = (cores[randint(0,(len(cores)-1))])   #soteia uma cor por jogador
        jogadores[i].update(cor = cor)               #adiciona a cor ao dict
        cores.remove(cor) #para não repetir as cores

        ######################### ADD INDEX LIST OF DICT AND FEEDING THE CONTROL FOR MODULE STATISTICS
        aux_list.append({'ident': len(aux_list), 'names': jogadores[i]['nome'], 'win': 0, 'lose': 0})
        control_list.append(jogadores[i]['nome'])
        jgReinicio = jogadores[:]
        ######################### MODULESTATISTICS
    return jogadores

################3

def definirJogadores2():  # define quantos jogadores irão jogar e atribui a cada um deles - uma palavra, a qttd de erros e uma cor
    global jgReinicio
    print()
    jogadores = jgReinicio[:]
    for i, valor_dicio in enumerate(jgReinicio):
        
        sorteio = Palavra()
        sorteio.setPalavra(listaPalavras)
        palavraSorteada = sorteio.getPalavra()
        jogadores[i].update(erros=0)  # cria um dict e add a chave erros
        palavraSorteada = sorteio.getPalavra()
        jogadores[i].update(palavra = palavraSorteada)   #adiciona a palavra secreta ao dict
        sorteio.setLetrasEscondidas(palavraSorteada)
        letrasAcertadas = sorteio.getLetrasEscondidas()
        jogadores[i].update(letrasAcertadas = letrasAcertadas)  #adiciona as letras acertadas ao dict
        # print(jogadores)
    ######################### ADD INDEX LIST OF DICT AND FEEDING THE CONTROL FOR MODULE STATISTICS
    aux_list.append({'ident': len(aux_list), 'names': jogadores[i]['nome'], 'win': 0, 'lose': 0})
    control_list.append(jogadores[i]['nome'])
    jgReinicio = jogadores[:]
    ######################### MODULESTATISTICS
    return jogadores

################


def reiniciaJogo():
    global vez, jogadores
    print('1 - Reiniciar Partida')
    print('2 - Reiniciar Jogo')
    print('3 - Estatísiticas')
    print('4 - Voltar para Menu Principal')
    opc = int(input('Digite sua opcao: '))
    if opc == 1:
        jogadores = jgReinicio
        vez = 0
        bemVindos()
        definirJogadores2()
        inicioJogo()
    if opc == 2:
        vez = 0
        rodarJogo()
    if opc == 3:
        s.view_statistics2(aux_list)
        reiniciaJogo()
    if opc == 4:
        navegaMenu()
    else:
        print('Opção inválida')
        reiniciaJogo()


def rodarJogadores():           # para rodar os jogadores caso perde ou ganha
    global vez
    if vez > len(jogadores) - 1: #se o indice chega ao fim
        vez = 0                     #volta ao primeiro jogador (indice 0)

    titulos(f'Vez do jogador {jogadores[vez]["nome"]}', jogadores[vez]['cor'])
    desenha_forca(jogadores[vez]['erros'])
    print(f'Restam {6 - jogadores[vez]["erros"]} tentativas')
    print(jogadores[vez]['letrasAcertadas'])


def tentativa():
    while(True):
        chute = input('\nQual letra ou palavra? ').strip().upper()
        confirmar = input(
            "\n Confirma? \n Pressione enter para prosseguir ou digite 'n' e pressione enter para cancelar, .\n"
            )

        if chute == jogadores[vez]['palavra']:
            jogadores[vez]['letrasAcertadas'] = chute.upper()
            acertouLetra(chute)

        elif confirmar != 'n':
            if len(chute) != 1:
                print("Por favor, digite apenas uma letra por vez.")
                tentativa()

            # verifica se a letra pertence ao alfabeto
            elif re.match("[A-Za-z]", chute) is None:
                print(f"{chute} é um caracter inválido, tente novamente!")
                continue
            break
        else:
            continue
    return chute

  
def imprimePodio():
    global podio
    if len(podio[0]) == 0:
        print('Não houveram ganhadores')
    else:
        colocacao = 1
        for i in podio[0]:
            print(f'{colocacao}º lugar', end= ' - ')
            print(i)
            colocacao += 1

    ######################### LAUCH INFORMATION AND INVOCATION OF FUNCTION STATISTICS2
    podio = [[], []]
    print('\n' * 2)
    reiniciaJogo()
    ######################### MODULESTATISTICS

def acertouLetra(tentativa):    
        index = 0
        if tentativa in jogadores[vez]['letrasAcertadas']:
            print('Letra já informada, escolha outra')

        for letra in jogadores[vez]['palavra']:
            if (tentativa.upper() == letra.upper()):
                jogadores[vez]['letrasAcertadas'][index] = letra                
            index += 1
        print(f'Bela tentativa, adicionando {tentativa}')
        print(jogadores[vez]['letrasAcertadas'])
            
        if marcador not in jogadores[vez]['letrasAcertadas']:
            colorir(f'{jogadores[vez]["nome"]} acertou a palavra', '\033[32m')
            podio[0].append(jogadores[vez]['nome'])                     #adiciona o nome ao pódio

            ######################### UPDATE VALUE IN KEY -WIN- FROM THE DICT FOR MODULE STATISTICS
            aux_list[control_list.index(jogadores[vez]['nome'])]['win'] += 1
            ######################### MODULESTATISTICS

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
        colorir(f'{jogadores[vez]["nome"]} foi enforcado. A palavra era {jogadores[vez]["palavra"] }')          
        
        podio[1].append(jogadores[vez]['nome'])  #adiciona o nome ao pódio

        ######################### UPDATE VALUE IN KEY -LOSE- FROM THE DICT FOR MODULE STATISTICS
        aux_list[control_list.index(jogadores[vez]['nome'])]['lose'] += 1
        ######################### MODULESTATISTICS

        jogadores.remove(jogadores[vez]) #remove perdedor da lista de jogadores
        
        if len(jogadores) == 0:
            colorir('Fim de Jogo')
            imprimePodio()
        else:
            rodarJogadores()
    
    else:
        vez += 1
        colorir('Passou a vez')
        rodarJogadores()


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
    definirJogadores()
    inicioJogo()


def navegaMenu():
    opc = menu_inicial()
    if opc==1:
        rodarJogo()
    elif opc==2:
        s.view_statistics2(aux_list)
        navegaMenu()
    elif opc==3:
        exit()
    else:
        print('Opção inválida')
        navegaMenu()

navegaMenu()

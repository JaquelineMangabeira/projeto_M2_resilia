from time import sleep
from sys import exit

def  bemVindos ():
    print( """
                  , -.
             ()   \           A época mais mágica do ano chegou com um jogo que 
             /    \             vem com cheiro de rabanada no ar e filmes
           _/______\_                 clássicos para maratonar.
          (__________)            
          (/  @  @  \)       Se você não for o Grinch, O jogo Palavras Natalinas
          (`._,()._,')         vai tornar a sua noite de natal muito especial  
          (  `-'`-'  )          e cheia de união com a família (ou não rs.)            
           \        /
            \,,,,,,/                   Divirta-se e Boa sorte!
              """)



sleep(2)

def menu_inicial():
    print('1 - Iniciar jogo \n2 - Estísticas \n3 - Sair')
    opcao = int(input('Escolha uma opção: '))
    if opcao==1:
        rodarJogo()

    elif opcao==2:
        view_statistics2(d_p)

    elif opcao==3:
        exit()

    else:
        print('Opção inválida')
        menu_inicial()

bemVindos()

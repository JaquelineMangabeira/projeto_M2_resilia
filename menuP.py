from time import sleep

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
  menu_inicial()

def menu_inicial():
  print('1 - Iniciar jogo \n2 - Estísticas \n3 - Sair')
  opcao = int(input('Escolha uma opção: '))
  return opcao

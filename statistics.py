# Game - Forca
# Tema Natalino
# Projeto de Finalizacao do Módulo II
# Curso de Data Analytics - Resília


# Import modules

# Lib for selection from colors
from colors import cores as co
from time import sleep as sl

# Definiction of function for module visualization --statistics


def print_format(txt):
    len_txt = len(txt)
    print(f"{co(4)}{'-=' * len_txt}{co(-1)}")
    print(f'{co(13)}{txt:^{len_txt * 2}}{co(-1)}')
    print(f"{co(4)}{'-=' * len_txt}{co(-1)}")


def view_statistics2(d_p):  # Function for visualization from the datas of game
    print_format('- ESTATÍSTICA | SCORE -')
    print(f'{co(13)}{"":<2}{"ID":<3}{"ORD.":<5}{"NOME":<25}{"Win|Los":<10} {co(-1)}')

    # Categorizacao de dict
    lista_aux = [valor_lista['win'] for valor_lista in d_p]
    dicio_aux = dict()
    for index, value in enumerate(lista_aux):
        dicio_aux[index] = value
    lta = sorted(dicio_aux.items(), key=lambda x: x[1], reverse=True)

    print(f"{co(4)}{'--' * 23}{co(-1)}")
    for i in range(len(d_p)):
        if i % 2 == 0:
            sl(0.4)
            print(f'{co(4)}{"|":<2}{d_p[lta[i][0]]["ident"]:<3}{i+1:<5}{d_p[lta[i][0]]["names"]:<25}{str(d_p[lta[i][0]]["win"]) + " -- " + str(d_p[lta[i][0]]["lose"]):<9} {"|":<1}{co(-1)}')
        else:
            sl(0.4)
            print(f'{"|":<2}{d_p[lta[i][0]]["ident"]:<3}{i+1:<5}{d_p[lta[i][0]]["names"]:<25}{str(d_p[lta[i][0]]["win"]) + " -- " + str(d_p[lta[i][0]]["lose"]):<9} {"|":<1}')
    print(f"{co(13)}{'--' * 23}{co(-1)}")

    


# Data application for test

# view_statistics2([{'ident': 0, 'names': 'Brunna', 'win': 3, 'lose': 0}, {'ident': 1, 'names': 'nome2', 'win': 0, 'lose': 2}, {'ident': 3, 'names': 'nome3', 'win': 1, 'lose': 0}, {'ident': 3, 'names': 'Jonathas', 'win': 3, 'lose': 1}])

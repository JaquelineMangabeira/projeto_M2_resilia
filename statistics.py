# Game - Forca
# Tema Natalino
# Projeto de Finalizacao do Módulo II
# Curso de Data Analytics - Resília


# Definiction of function for module visualization --statistics

def print_format(txt):
    len_txt = len(txt)
    print('-=' * len_txt)
    print(f'{txt:^{len_txt * 2}}')
    print('-=' * len_txt)


def view_statistics2(d_p):  # Function for visualization from the datas of game
    print_format('PAINEL ESTATÌSTICO SCORE')
    print(f'{"":<2}{"ID":<8}{"NOME":<25}{"Win|Los":<10}')
    print('--' * 23)
    for ind in d_p:
        print(f'{"+":<2}{ind["ident"]:<8}{ind["names"]:<25}{str(ind["win"]) + " -- " + str(ind["lose"]):<9}{"+":<1}')
    print('--' * 23)


# Data application for test
# view_statistics2([{'ident': 0, 'names': 'nome', 'win': 0, 'lose': 0}, {'ident': 1, 'names': 'nome2', 'win': 0, 'lose': 2}, {'ident': 3, 'names': 'nome3', 'win': 1, 'lose': 0}])

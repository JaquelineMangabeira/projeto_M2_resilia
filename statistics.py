# Game - Forca
# Tema Natalino
# Projeto de Finalizacao do Módulo II
# Curso de Data Analytics - Resília


# Definiction of function for módule visualization --statistics

def print_format(txt):
    len_txt = len(txt)
    print('-=' * len_txt)
    print(f'{txt:^{len_txt * 2}}')
    print('-=' * len_txt)


def view_statistics2(d_p):  # Function for visualization from the datas of game
    print_format('PAINEL ESTATÌSTICO SCORE')
    print(f'{"":<2}{"ID":<8}{"NOME":<25}{"Win|Los":<10}')
    print('--' * 23)
    for ind in range(len(d_p['win'])):
        print(f'{"+":<2}{d_p["ident"][ind]:<8}{d_p["names"][ind]:<25}{str(d_p["win"][ind]) + " -- " + str(d_p["lose"][ind]):<9}{"+":<1}')
    print('--' * 23)


# Data application for test

'''ident = [111, 222, 333, 444]
names = ['Brunna', 'Jaqueline', 'Laion', 'Jonathas']
win = [5, 5, 3, 2]
lose = [0, 0, 1, 2]
dic = {'ident': ident, 'names': names, 'win': win, 'lose': lose}'''

view_statistics2(dic)


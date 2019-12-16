#  File:
#        home.py
#
#  Module:
#        home
#
#  Authors: Arthur Camargo and Pablo Rodrigues
#
#  Description: implements home of the system
#
##############################################################################
#  Create Date: 12.12.2019
#
#  Last Modified Date:
#       09.12.2019
#
#  Additional Comments:
##############################################################################
import psycopg2
import os
import lists as l
import mybooks as mb
import groups as gp
import friends as fr
import profile as pf
import searchbooks as sb
import events as ev
import statistic as st

def home(userdata):
    """ Implements the homepage of system """

    logged = True
    msg_welcomef = "Seja bem-vinda, " + userdata[1] + ".\n\n"
    msg_welcomem = "Seja bem-vindo, " + userdata[1] + ".\n\n"

    # Sections definition
    my_books = "[1] Meus Livros"
    search_books = "[2] Pesquisar livros"
    lists = "[3] Listas"
    groups = "[4] Grupos"
    friends = "[5] Amigos"
    statistics = "[6] Estatísticas"
    profile = "[7] Perfil"
    quit = "[8] Sair"

    os.system('clear')

    # Welcome message treatment
    if userdata[4] == 'F':
        print(msg_welcomef)
    else:
        print(msg_welcomem)

    # Execute the program while the user don't press quit(7)
    while logged:
        section = input(my_books+'\n'+search_books+'\n'+lists+'\n'+groups+'\n'+friends+'\n'+statistics+'\n'+profile+'\n'+quit+'\n>> ')

        if section == '1':
            mb.mybooks_page(userdata[0])
        elif section == '2':
            sb.searchbooks_page(userdata[0])
        elif section == '3':
            l.lists_page(userdata)
        elif section == '4':
            gp.groups_page(userdata)
        elif section == '5':
            fr.friends_page(userdata[0])
        elif section == '6':
            st.stats_page(userdata)
        elif section == '7':
            pf.profile_page(userdata[0])
        elif section == '8':
            logged = False
        else:
            print()
        os.system('clear')

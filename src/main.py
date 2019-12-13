#  File:
#        main.py
#
#  Module:
#        main
#
#  Authors: Arthur Camargo and Pablo Rodrigues
#
#  Description:
#
##############################################################################
#  Create Date: 05.12.2019
#
#  Last Modified Date:
#       09.12.2019
#
#  Additional Comments:
##############################################################################
import os        # Auxiliary module to use unix commands
import login as lg
import register as rg

def start():
    """ Display the menu and take the user input """

    absolute_quit = False
    msg_return_start = "Pressione qualquer botão para voltar para a página inicial..."
    msg_entry_text = "1. Entrar\t2. Criar uma nova conta\n:"

    while not absolute_quit:
        validating = True

        # Take the user input and validates
        while validating:
            user_input = input(msg_entry_text)
            if user_input == '1':
                validating = False
            elif user_input == '2':
                validating = False
            else:
                os.system('clear')
                print("Insira uma opcao válida.")

        if user_input == '1':
            lg.login()
        else:
            rg.create_account()

            botton = input(msg_return_start)
            os.system('clear')


start()

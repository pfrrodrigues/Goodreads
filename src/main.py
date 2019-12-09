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
#       05.12.2019
#
#  Additional Comments:
##############################################################################
import psycopg2
import os

# Connect to the database
conn = psycopg2.connect(host='127.0.0.1',
                        password='12345',
                        user='postgres',
                        dbname='actual')
# Create a cursor
cur = conn.cursor()

# Check user password
def passwordcheck(user_data):

    if user_data:
        while passwd != user_data[2]:
            passwd = input("Senha invalida. Por favor, insira novamente sua senha: ")

            cur.execute("SELECT email, nome, senha FROM leitor WHERE email = %s;", (email,));
            query = cur.fetchone()

        print('Bem-vindo, '+ query[1] + '.')
        break
    else:
        os.system('clear')
        print("Email invalido. Por favor, insira novamente seu email.")

# Implement user login
def loggin():

    while (True):
        email = input("email: ")
        passwd = input("password: ")
        cur.execute("SELECT email, nome, senha FROM leitor WHERE email = %s;", (email,));
        user_data = cur.fetchone()

        passwordcheck(user_data)

# Validate the options
def option_ok(user_input):

    if user_input != '1' and user_input != '2':
        return False
    else:
        return True

# Display the menu
def exibition():
    while (True):
        user_input = input("1. Entrar na minha conta.\n2.Criar uma nova conta.\n")
        if option_ok(user_input):
            break
        else:
            os.system('clear')
            print("Insira uma opcao válida.")

    if (user_input) == '1':
        loggin()
    else:
        create_account()


exibition()









# Make changes in database
# conn.commit()

# Close the communication with the database
cur.close()
conn.close()

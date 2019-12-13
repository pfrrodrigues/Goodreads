#  File:
#        login.py
#
#  Module:
#        login
#
#  Authors: Arthur Camargo and Pablo Rodrigues
#
#  Description: implements login functions
#
##############################################################################
#  Create Date: 12.12.2019
#
#  Last Modified Date:
#       09.12.2019
#
#  Additional Comments:
##############################################################################
import psycopg2  # Module to connect to the database
import os        # Auxiliar module to use unix commands
from passlib.hash import pbkdf2_sha256 # Module to obtain hash for passwords
import home as hm

# Implements user login
def login():
    """ Implements user login """

    # Connect to the database
    conn = psycopg2.connect(host='127.0.0.1',
                            password='12345',
                            user='postgres',
                            dbname='actual')
    # Create a cursor
    cur = conn.cursor()

    validating = True
    msg_incorrect_passwd = "Senha incorreta. Por favor, verifique seus dados com atencao."
    msg_incorrect_email = "Email não existe. Por favor, verifique seus dados com atencao."

    while validating:
        email = input("Email: ")
        passwd = input("Senha: ")

        cur.execute("SELECT email, nome, senha, leitor_tipo, sexo FROM leitor WHERE email = %s;", (email,))
        db_data = cur.fetchone() # Returns a tuple if email exists

        if db_data:
            if (pbkdf2_sha256.verify(passwd, db_data[2])):
                validating = False
            else:
                print(msg_incorrect_passwd)
        else:
            print(msg_incorrect_email)

    # Close the connection with the database
    cur.close()
    conn.close()

    # Go to the homepage
    hm.home(db_data)

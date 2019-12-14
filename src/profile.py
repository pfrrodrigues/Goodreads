#  File:
#        profile.py
#
#  Module:
#        profile
#
#  Authors: Arthur Camargo and Pablo Rodrigues
#
#  Description:
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
from prettytable import PrettyTable
from passlib.hash import pbkdf2_sha256 # Module to obtain hash for passwords


def profile_page(email):
    """ Shows and treats user information """

    # Connect to the database
    conn = psycopg2.connect(host='127.0.0.1',
                            password='12345',
                            user='postgres',
                            dbname='actual')
    # Create a cursor
    cur = conn.cursor()

    # Auxiliary strings
    change_passwd = "[1] Alterar senha"
    delete_account = "[2] Excluir conta"
    rtrn = "[3] Voltar"

    # Get user information
    cur.execute("SELECT * FROM leitor WHERE email=%s", (email,))
    user = cur.fetchall()

    # Get the country of user
    cur.execute("SELECT nome FROM pais WHERE codpais = %s", (user[0][6],))
    country = cur.fetchone()

    # Print the table with user information
    table = PrettyTable(['Email', 'Nome', 'Sexo', 'Nascimento(YYYY-MM-DD)', 'Pais'])
    table.add_row([user[0][0], user[0][1], user[0][3], user[0][4], country[0]])
    print(table)

    while True:
        option = input('\n'+change_passwd+'\n'+delete_account+'\n'+rtrn+'\n>> ')

        if int(option) < 1 or int(option) > 3:
            continue
        else:
            if option == '1':
                os.system('clear')
                processing_passwd = True

                while processing_passwd:
                    actual_passwd = input("Informe a sua senha atual: ")

                    if (pbkdf2_sha256.verify(actual_passwd, user[0][2])):
                        processing_passwd = False
                    else:
                        print("A senha fornecida não confere.")

                processing_new_passwd = True

                while processing_new_passwd:
                    new_passwd = input("Insira a sua nova senha: ")
                    repeat_npasswd = input("Insira a nova senha novamente: ")

                    if new_passwd == repeat_npasswd:
                        processing_new_passwd = False
                    else:
                        print("Senhas não conferem.")
                        continue

                password = pbkdf2_sha256.hash(new_passwd)

                cur.execute("UPDATE leitor SET senha = %s WHERE email = %s", (password, email,))
                conn.commit()

                press_exit = input("SENHA ALTERADA COM SUCESSO.\nPRESSIONE UMA TECLA PARA LOGAR COM A NOVA SENHA...")
                os.system('exit')
                os.system('clear')
                os.system('python3 main.py')

            # Delete account
            elif option == '2':

                processing_delete = True
                while processing_delete:
                    os.system('clear')
                    password = input("Informe a sua senha: ")

                    if (pbkdf2_sha256.verify(password, user[0][2])):
                        processing_delete = False
                    else:
                        print("A senha fornecida não confere.")
                        continue

                while True:
                    warning_option = input("Tem certeza que deseja excluir sua conta?\n  [S] SIM\n  [C] CANCELAR\n>> ")

                    if (warning_option.upper() != 'S') and (warning_option.upper() != 'C'):
                        print("Digite uma opção válida.")
                    else:
                        # Delete account
                        if warning_option.upper() == 'S':
                            cur.execute("DELETE FROM leitor WHERE email = %s;", (email,))
                            cur.commit()
                            break
                        # Abort account exclusion
                        else:
                            break
            # Return
            else:
                break

    # Close the connection with the database
    cur.close()
    conn.close()

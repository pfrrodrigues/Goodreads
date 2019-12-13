#  File:
#        register.py
#
#  Module:
#        register
#
#  Authors: Arthur Camargo and Pablo Rodrigues
#
#  Description: contain neccessary functions to create a user account
#
##############################################################################
#  Create Date: 12.12.2019
#
#  Last Modified Date:
#       09.12.2019
#
#  Additional Comments:
##############################################################################
import os
import psycopg2
from passlib.hash import pbkdf2_sha256 # Module to obtain hash for passwords


def set_country(username):
    """ Set the country of user """

    # Connect to the database
    conn = psycopg2.connect(host='127.0.0.1',
                            password='12345',
                            user='postgres',
                            dbname='actual')
    # Create a cursor
    cur = conn.cursor()

    msg_country = "Com que letra comeca seu pais de origem, " + username + "?\n: "
    msg_country_code = "Informe o codigo do seu pais de origem: "
    msg_country_not_found = "Desculpe, ouve problemas no processamento do código do país"

    initial_letter = (input(msg_country)).upper()

    cur.execute("SELECT codpais, nome FROM pais WHERE nome like %s;", (initial_letter+'%',))
    countries = cur.fetchall()

    if countries:
        for country in countries:
            print("Código do país: [" + str(country[0]) + "]  País: " + country[1])

        code = input(msg_country_code)
    else:
        print(msg_country_not_found)

    # Close the connection with the database
    cur.close()
    conn.close()

    return code


def create_account():
    """ Creates a user account """

    # Connect to the database
    conn = psycopg2.connect(host='127.0.0.1',
                            password='12345',
                            user='postgres',
                            dbname='actual')
    # Create a cursor
    cur = conn.cursor()

    processing_email = True
    processing_sex = True

    # Messages definition
    msg_header = "::::::::REGISTRO DE NOVO USUÁRIO::::::::"
    msg_used_email = "Email já cadastrado. Por favor, forneca outro email de sua escolha."
    msg_invalid_sex = "Entrada invalida. Por favor, insira novamente um sexo valido."
    msg_success = "Seu cadastro foi efetuado com sucesso."
    msg_error_register = "Desculpe, houve um erro ao cadastrar a sua conta."

    os.system('clear')
    print(msg_header)

    name = (input("Nome: ")).title()

    while processing_email:
        email = input("Email: ")

        cur.execute("SELECT email FROM leitor WHERE email = %s;", (email,))
        email_already_used = cur.fetchone()

        if email_already_used:
            print(msg_used_email)
        else:
            processing_email = False

    # Convert password into a sha256 hash
    password = pbkdf2_sha256.hash(input("Senha: "))

    while processing_sex:
        sex = (input("Sexo: F/f - Feminino     M/m - Masculino: ")).upper()

        if (sex == 'F') or (sex == 'M'):
            processing_sex=False
        else:
            print(msg_invalid_sex)

    birth = input("Informe a data do seu nascimento(YYYY-MM-DD): ")
    country = set_country(name)

    cur.execute("INSERT INTO leitor VALUES(%s, %s, %s, %s, %s,'1', %s);",
                (email, name, password, sex,birth,country,))

    # Upload the changes to the database
    conn.commit()

    cur.execute("SELECT email FROM Leitor where email = %s", (email,))
    check_upload = cur.fetchone()

    if check_upload:
        print(msg_success)
    else:
        print(msg_error_register)

    # Close the connection with the database
    cur.close()
    conn.close()

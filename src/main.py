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
import psycopg2
import os

# Connect to the database
conn = psycopg2.connect(host='127.0.0.1',
                        password='12345',
                        user='postgres',
                        dbname='test-goodreads')
# Create a cursor
cur = conn.cursor()

# Check user password
def passwordcheck(user_data, email, passwd):
    while passwd != user_data[2]:
        passwd = input("Senha invalida. Por favor, insira novamente sua senha: ")

        cur.execute("SELECT email, nome, senha FROM leitor WHERE email = %s;", (email,));
        query = cur.fetchone()

    print('Bem-vindo, '+ user_data[1] + '.')

# Implement user login
def login():
    while (True):
        email = input("email: ")
        passwd = input("password: ")
        cur.execute("SELECT email, nome, senha FROM leitor WHERE email = %s;", (email,));
        user_data = cur.fetchone()

        if not user_data:
            print("Email invalido. Por favor, insira novamente seu email.")
        else:
            passwordcheck(user_data, email, passwd)
            break


def country_def(name):
    initial = (input("Com que letra comeca seu pais de origem, " + name + "?: ")).upper()
    print(initial+'%')
    cur.execute("SELECT codpais, nome FROM pais WHERE nome like %s;", (initial+'%',))
    countries = cur.fetchall()

    if countries:
        for country in countries:
            print("code: [" + str(country[0]) + "]  country: " + country[1])
        cod = input("Informe o codigo do seu pais de origem: ")
    else:
        print("Desculpe, nao temos o codigo do seu pais, " + name + ". Iremos averiguar.")
        # apenas temporario
        cod = '1'
    return cod

#
def create_account():
    os.system('clear')
    print("CADASTRO")

    email_processing = True

    while email_processing:
        name = (input("Nome: ")).title()
        email = input("Email: ")

        cur.execute("SELECT email FROM Leitor WHERE email=%s;", (email,))
        list_of_emails = cur.fetchone()

        if list_of_emails is not None:
            print("Conta com este email ja existe. Por favor, forneca outro email de sua escolha.")
        else:
            email_processing = False

    # inicialmente sem validação, eventualmente iremos validar.
    password = input("Senha: ")

    processing_sex = True
    while(processing_sex):
        sexo = (input("Sexo: F/f - Feminino     M/m - Masculino: ")).upper()

        if sexo == 'F':
            processing_sex=False
        elif sexo == 'M':
            processing_sex=False
        else:
            print("Entrada invalida. Por favor, insira novamente um sexo valido.")

    nasc = input("Informe a data do seu nascimento(YYYY-MM-DD): ")

    country = country_def(name)

    cur.execute("INSERT INTO Leitor VALUES(%s, %s, %s, %s, %s,'1', %s);",(email, name, password,sexo,nasc,country,))
    conn.commit()
    cur.execute("SELECT email FROM Leitor where email = %s", (email,))
    check = cur.fetchone()

    if check:
        print("Parabens! Seu cadastro foi efetuado com sucesso.")
    else:
        print("Desculpe, houve um erro ao cadastrar a sua conta.")

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
        login()
    else:
        create_account()

exibition()

# Make changes in database
# conn.commit()

# Close the communication with the database
cur.close()
conn.close()

""" Pagina que trata dos grupos """

import psycopg2  # Module to connect to the database
import os        # Auxiliar module to use unix commands
import home as hm
from prettytable import PrettyTable

new_line = "\n"
def your_groups(user, conn, cursor):
    """ Pagina onde contem os grupos que um usuario participa """
    t = PrettyTable(['Opção', 'Nome', 'Tags', 'Creator'])#cabecario da tabela

    cursor.execute("""SELECT * FROM show_my_groups(%s)""", (user[0],))
    groups = cursor.fetchall()

    cnt_group = 1
    for group in groups:
        cursor.execute("SELECT tag FROM show_groups WHERE codigo = %s ",(group[0],))
        tags = cursor.fetchall()
        pretty_tags = ''
        for tag in tags:
            pretty_tags += '#' + str(tag[0]) + ", "
        t.add_row([str(cnt_group), group[1], pretty_tags, group[2]])
        cnt_group += 1
    print(t)
    pass

def your_created_groups(user, conn, cursor):
    """ Pagina com os grupos que foram criados pelo user """

    t = PrettyTable(['Opção', 'Nome', 'Tags', 'Creator'])#cabecario da tabela

    cursor.execute("""SELECT DISTINCT codigo, grupo, criador
                        FROM show_groups
                        WHERE criador = %s """, (user[0],))
    groups = cursor.fetchall()

    cnt_group = 1
    for group in groups:
        cursor.execute("SELECT tag FROM show_groups WHERE codigo = %s ",(group[0],))
        tags = cursor.fetchall()
        pretty_tags = ''
        for tag in tags:
            pretty_tags += '#' + str(tag[0]) + ", "
        t.add_row([str(cnt_group), group[1], pretty_tags, group[2]])
        cnt_group += 1
    print(t)

    msg = "Você deseja:" + new_line
    adicionar = "[1] Criar um grupo" + new_line
    quit = "[q] Voltar" + new_line + ">>"

    msg += adicionar + quit

    logged = True
    while logged:
        opt = input(msg)
        if opt == '1':
            create_group_menu(user, conn, cursor)
        elif opt == 'q':
            logged = False
        else:
            print("Comando inválido" + new_line)

def create_group(nome_grupo, user, conn, cursor):
    """ cria um grupo """
    cursor.execute("INSERT INTO grupo(nome, fk_leitor_email) VALUES (%s, %s) RETURNING codGrupo", (nome_grupo, user[0],))
    codGrupo = cursor.fetchone()
    return codGrupo

def create_group_menu(user, conn, cursor):
    """ Pagina para criar grupos """

    os.system('clear')

    nome = "Qual sera o nome do grupo:" + new_line + ">>"
    nome_grupo = input(nome)
    cod_grupo = create_group(nome_grupo, user, conn, cursor)

    tags = "Qual serao as tags do grupo(separadas por virgula):" + new_line + ">>"
    tags_grupo = input(tags)
    tags_grupo = tags_grupo.split(',')
    for tag in tags_grupo:

        cursor.execute("SELECT codtagg FROM tag_grupo WHERE tagg = %s ", (tag,))
        codtagg = cursor.fetchone()

        if not codtagg:
            cursor.execute("INSERT into tag_grupo(tagg) VALUES (%s) RETURNING codtagg", (tag,))
            conn.commit()
            codtagg = cursor.fetchone()

        cursor.execute("INSERT into posse_tagg VALUES (%s, %s)", (cod_grupo, codtagg,))
        conn.commit()

def all_groups(cursor):
    """ Pagina que mostra todos os grupos """

    t = PrettyTable(['Opção', 'Nome', 'Tags', 'Creator'])#cabecario da tabela

    cursor.execute("SELECT DISTINCT codigo, grupo, criador FROM show_groups")
    groups = cursor.fetchall()

    cnt_group = 1
    for group in groups:
        cursor.execute("SELECT tag FROM show_groups WHERE codigo = %s ",(group[0],))
        tags = cursor.fetchall()
        pretty_tags = ''
        for tag in tags:
            pretty_tags += '#' + str(tag[0]) + ", "
        t.add_row([str(cnt_group), group[1], pretty_tags, group[2]])
        cnt_group += 1
    print(t)

def groups_page(current_user):
    """ Pagina principal dos grupos """

    conn = psycopg2.connect(host='127.0.0.1',
                            password='12345',
                            user='postgres',
                            dbname='actual')

    cursor = conn.cursor()

    os.system('clear')
    msg = "O que você deseja:" + new_line
    criar = "[1] Ver seus grupos" + new_line
    participa = "[2] Ver os grupos que você participa" + new_line
    allg = "[3] Vizualizar todos os grupos" + new_line
    quit = "[q] Voltar" + new_line + ">>"

    msg += criar +  participa + allg + quit

    logged = True

    while logged:
        opt = input(msg)

        if opt == '1':
            your_created_groups(current_user, conn, cursor)
        elif opt == '2':
            your_groups(current_user, conn, cursor)
        elif opt == '3':
            all_groups(cursor)
        elif opt == 'q':
            logged = False

""" Pagina que trata das listas """

import psycopg2  # Module to connect to the database
import os        # Auxiliar module to use unix commands
from passlib.hash import pbkdf2_sha256 # Module to obtain hash for passwords
import home as hm
from prettytable import PrettyTable

def select_list(lista, cursor):
    os.system('clear')
    new_line = "\n"
    msg = "Pressione qualquer botão para voltar." + new_line
    quit = "[q] Voltar" + new_line + ">>"
    msg += quit

    cursor.execute("""SELECT fk_livro_isbn FROM lista
                      JOIN contem ON(lista.codlista = contem.fk_lista_codlista)
                      WHERE lista.codlista = %s """, (lista,))
    livros = cursor.fetchall()

    t = PrettyTable(['Opção', 'Titulo', 'Autor'])#cabecario da tabela

    counter_books = 1
    if livros:

        for book in livros:

            cursor.execute(""" select livro.isbn, livro.titulo, livro.imagem, e.nome, leitura.tipo as marcacao, leitura.classificacao as nota
                                   from livro
                                   left join leitura on (livro.isbn = leitura.fk_livro_isbn)
                                   join escrita on (livro.isbn=escrita.fk_livro_isbn)
                                   join leitor e on (escrita.fk_leitor_email=e.email)
                                   where livro.isbn = %s;
                                   """, (book[0],))
            book = cursor.fetchone()

            if book:
                t.add_row([str(counter_books), book[1], book[3]])
                counter_books += 1

        print(t)

    input(msg)
    os.system('clear')

def search_by_name(num_itens, cursor):
    """ Show the num_itens popular lists"""

    os.system('clear')
    new_line = "\n"
    msg = "Digite o nome da lista que deseja procurar:" + new_line + ">>"
    lista_nome = input(msg)


    t = PrettyTable(['Opção', 'Nome', 'Tags', 'Livros'])#cabecario da tabela

    cursor.execute("""SELECT lista.codlista, lista.nome FROM lista
                      WHERE lista.nome LIKE %s""", (lista_nome + '%',))
    lists = cursor.fetchall()

    counter_lists = 1
    for lista in lists:
        cursor.execute("""SELECT tagl FROM lista
                          JOIN posse_tagl ON (lista.codlista = posse_tagl.fk_lista_codlista)
                          JOIN tag_lista ON (posse_tagl.fk_tag_lista_codtagl = tag_lista.codtagl)
                          WHERE lista.codlista = %s""", (lista[0],))
        your_tagls = cursor.fetchall()

        cursor.execute("""SELECT livro.titulo FROM lista
                          JOIN contem ON (lista.codlista = contem.fk_lista_codlista)
                          JOIN livro ON (contem.fk_livro_isbn= livro.isbn)
                          WHERE lista.codlista = %s """, (lista[0],))
        livros = cursor.fetchall()

        pretty_books = ''#Printa os livros mais bonitos
        for livro in livros:
            pretty_books += str(livro[0]) + new_line

        pretty_tags = '' #printa mais bonitos a tag
        for tag in your_tagls:

            pretty_tags += '#'
            pretty_tags += str(tag[0]) + ', '#adiciona o newline com a tag

        t.add_row([str(counter_lists), lista[1], str(pretty_tags), str(pretty_books)])
        counter_lists += 1

    logged = True

    while logged:

        print(t) #Printa lista

        msg = "Para ver os livros de alguma lista pressione a sua Opção" + new_line
        quit ="[q] Voltar" + new_line + ">>"
        msg += quit

        opt = input(msg)
        if opt == 'q':
            logged = False
        elif opt.isdecimal():
            opt = int(opt)
            if opt > 0 and opt < counter_lists:
                select_list(lists[opt-1][0], cursor)
        else:
            print("Commando inválido" + new_line)

def search_by_tag(num_itens, cursor):
    """ Procura uma lista por suas tags """
    os.system('clear')
    new_line = "\n"
    msg = "Digite o nome da tag que deseja procurar:" + new_line + ">>"
    lista_nome = input(msg)


    t = PrettyTable(['Opção', 'Nome', 'Tags', 'Livros'])#cabecario da tabela

    cursor.execute("""SELECT lista.codlista, lista.nome FROM lista
                      JOIN posse_tagl ON (lista.codlista = posse_tagl.fk_lista_codlista)
                      JOIN tag_lista ON (posse_tagl.fk_tag_lista_codtagl = tag_lista.codtagl)
                      WHERE tag_lista.tagl LIKE %s""", (lista_nome + '%',))
    lists = cursor.fetchall()

    counter_lists = 1
    for lista in lists:
        cursor.execute("""SELECT tagl FROM lista
                          JOIN posse_tagl ON (lista.codlista = posse_tagl.fk_lista_codlista)
                          JOIN tag_lista ON (posse_tagl.fk_tag_lista_codtagl = tag_lista.codtagl)
                          WHERE lista.codlista = %s""", (lista[0],))
        your_tagls = cursor.fetchall()

        cursor.execute("""SELECT livro.titulo FROM lista
                          JOIN contem ON (lista.codlista = contem.fk_lista_codlista)
                          JOIN livro ON (contem.fk_livro_isbn= livro.isbn)
                          WHERE lista.codlista = %s """, (lista[0],))
        livros = cursor.fetchall()

        pretty_books = ''#Printa os livros mais bonitos
        for livro in livros:
            pretty_books += str(livro[0]) + new_line

        pretty_tags = '' #printa mais bonitos a tag
        for tag in your_tagls:

            pretty_tags += '#'
            pretty_tags += str(tag[0]) + ', '#adiciona o newline com a tag

        t.add_row([str(counter_lists), lista[1], str(pretty_tags), str(pretty_books)])
        counter_lists += 1

    logged = True

    while logged:

        print(t) #Printa lista

        msg = "Para ver os livros de alguma lista pressione a sua Opção" + new_line
        quit ="[q] Voltar" + new_line + ">>"
        msg += quit

        opt = input(msg)
        if opt == 'q':
            logged = False
        elif opt.isdecimal():
            opt = int(opt)
            if opt > 0 and opt < counter_lists:
                select_list(lists[opt-1][0], cursor)
        else:
            print("Commando inválido" + new_line)

def pesquisar_livros(livros, cursor):
    """Pagina para pesquisar livros a fim de adicionar em uma lista """

    new_line = "\n"
    cursor.execute("""SELECT livro.isbn FROM livro
                      WHERE livro.titulo LIKE %s """, (livros + '%',))
    livros = cursor.fetchall()

    counter_books = 1
    if livros:

        t = PrettyTable(['Opção', 'Título', 'Autor'])

        for book in livros:

                cursor.execute(""" select livro.isbn, livro.titulo, livro.imagem, e.nome, leitura.tipo as marcacao, leitura.classificacao as nota
                                   from livro
                                   left join leitura on (livro.isbn = leitura.fk_livro_isbn)
                                   join escrita on (livro.isbn=escrita.fk_livro_isbn)
                                   join leitor e on (escrita.fk_leitor_email=e.email)
                                   where livro.isbn = %s;
                                   """, (book[0],))
                book = cursor.fetchall()
                book = book[0]

                if book:
                    t.add_row([str(counter_books), book[1], book[3]])
                    counter_books += 1

        print(t)

    msg = "Para adicionar um livros selecione sua Opção" + new_line
    quit = "[q] Voltar" + new_line + ">>"
    msg += quit

    logged = True

    while logged:
        opt = input(msg)
        if opt == 'q':
            logged = False
        elif opt.isdecimal():
            opt = int(opt)
            if opt > 0 and opt < counter_books:
                return livros[opt-1][0]
        else:
            print("Commando inválido" + new_line)

def add_book_lista(isbn, codlista, conn, cursor):
    """ Adiciona um livro com uma dada isbn em uma lista """

    cursor.execute("""INSERT into contem(fk_lista_codlista, fk_livro_isbn)
                    VALUES (%s, %s)""", (codlista, isbn,))
    conn.commit()

def create_new_list(current_user, conn, cursor):
    """ Pagina para criar uma nova lista """
    logged = True
    new_line = '\n'

    while(logged):
        #Nome da lista
        msg = "Qual sera o nome da nova lista:" + new_line + ">>"
        lnome = input(msg)

        os.system('clear')

        cursor.execute("INSERT into lista(nome, fk_leitor_email) VALUES (%s, %s) RETURNING codlista", (lnome, current_user[0],))
        conn.commit()
        codlista = cursor.fetchone()

        #Tags
        msg = "Quais serão as tags da sua lista (separado por virgulas):" + new_line + ">>"
        tags = input(msg)
        tags = tags.split(',')

        os.system('clear')

        for tag in tags:
            cursor.execute("INSERT into tag_lista(tagl) VALUES (%s) RETURNING codtagl", (tag,))
            conn.commit()
            codtagl = cursor.fetchone()
            cursor.execute("INSERT into posse_tagl VALUES (%s, %s)", (codlista, codtagl,))
            conn.commit()


        #Livros da lista
        choosing = True

        while(choosing):
            msg = "Quais serão os livros da sua lista, digite um nome para adicionar:" + new_line + ">>"
            livro_nome = (input(msg)).title()
            add_isbn = pesquisar_livros(livro_nome, cursor)

            add_book_lista(add_isbn, codlista, conn, cursor)

            os.system('clear')

            wrong = True

            while(wrong):
                msg = "Deseja adicionar mais ? S/s, N/n" + new_line + ">>"
                opt = input(msg)


                if opt in ('n','N'):
                    wrong = False
                    choosing = False
                    logged = False
                elif opt in ('s','S'):
                    wrong = False
                else:
                    print("Commando incorreto..." + new_line)
                    input()

def choose_lists(lists):
    """ Pagina para escolher um numero de lista"""

    logged = True
    new_line = '\n'

    msg = "Selecione a lista que deseja editar:" + new_line
    quit ="[q] Voltar" + new_line + ">>"
    msg += quit

    while(logged):
        opt = input(msg)
        if opt == 'q':
            logged = False
        elif opt.isdecimal():
            opt = int(opt)
            if opt > 0 and opt <= len(lists):
                return lists[opt - 1][1]
        else:
            print("Commando inválido" + new_line)

def delete_lists(lists, conn, cursor):
    """ Deleta uma dada lista """

    cursor.execute("""DELETE FROM posse_tagl
                      WHERE fk_lista_codlista = %s""", (lists,))

    cursor.execute("""DELETE FROM contem
                      WHERE fk_lista_codlista = %s""", (lists,))

    cursor.execute("""DELETE FROM lista
                      WHERE lista.codlista = %s""", (lists,))

    cursor.execute("""DELETE FROM tag_lista
                      WHERE NOT EXISTS(SELECT * FROM posse_tagl
                                       WHERE fk_tag_lista_codtagl = codtagl)""")
    conn.commit()
    print("Lista deletada com sucesso ...")
    input()

def alter_lists(lists, conn, cursor):
    """ Altera uma dada lista """

    logged = True
    new_line = '\n'

    msg = "Voce deseja:" + new_line
    nome = "[1] Alterar o nome da lista" + new_line
    tags = "[2] Alterar as tags da lista" + new_line
    livros = "[3] Alterar os livros da lista" + new_line
    quit ="[q] Voltar" + new_line + ">>"

    msg += nome
    msg += tags
    msg += livros
    msg += quit


    while(logged):
        print_lista(lists, cursor)
        opt = input(msg)
        if opt == 'q':
            logged = False
        elif opt == '1':
            pass
            #alter_nome(lists)
        elif opt == '2':
            pass
            #alter_tags(lists)
        elif opt == '3':
            pass
            #alter_livros(lists)
        else:
            print("Commando inválido" + new_line)
    pass

def print_lista(lists, cursor):
    """ imprime uma lista dado seu codlista """

    new_line = "\n"

    t = PrettyTable(['Opção', 'Nome', 'Tags', 'Livros'])#cabecario da tabela

    cursor.execute("""SELECT lista.codlista, lista.nome FROM lista
                      WHERE lista.codlista = %s""", (lists,))
    lists = cursor.fetchall()

    counter_lists = 1
    for lista in lists:
        cursor.execute("""SELECT tagl FROM lista
                          JOIN posse_tagl ON (lista.codlista = posse_tagl.fk_lista_codlista)
                          JOIN tag_lista ON (posse_tagl.fk_tag_lista_codtagl = tag_lista.codtagl)
                          WHERE lista.codlista = %s""", (lista[0],))
        your_tagls = cursor.fetchall()

        cursor.execute("""SELECT livro.titulo FROM lista
                          JOIN contem ON (lista.codlista = contem.fk_lista_codlista)
                          JOIN livro ON (contem.fk_livro_isbn= livro.isbn)
                          WHERE lista.codlista = %s """, (lista[0],))
        livros = cursor.fetchall()

        pretty_books = ''#Printa os livros mais bonitos
        for livro in livros:
            pretty_books += str(livro[0]) + new_line

        pretty_tags = '' #printa mais bonitos a tag
        for tag in your_tagls:

            pretty_tags += '#'
            pretty_tags += str(tag[0]) + ', '#adiciona o newline com a tag

        t.add_row([str(counter_lists), lista[1], str(pretty_tags), str(pretty_books)])
        counter_lists += 1


        print(t) #Printa lista

def edit_lists_menu(lists, conn, cursor):
    """ Menu de edicao de lista """

    logged = True
    new_line = '\n'

    msg = "Voce deseja:" + new_line
    delete = "[1] Deletar essa lista" + new_line
    modify = "[2] Modificar essa lista" + new_line
    quit ="[q] Voltar" + new_line + ">>"

    msg += delete
    msg += modify
    msg += quit

    while(logged):

        print_lista(lists, cursor)

        opt = input(msg)
        if opt == 'q':
            logged = False
        elif opt == '1':
            delete_lists(lists, conn, cursor)
            logged = False
        elif opt == '2':
            alter_lists(lists, conn, cursor)
        else:
            print("Commando inválido" + new_line)

def show_your_lists(num_itens, current_user, conn, cursor):
    """ Show the lists that you follow """

    os.system('clear')
    logged = True
    new_line = '\n'

    while(logged):
        counter_lists = 1
        cursor.execute("""SELECT lista.nome, lista.codlista FROM lista
                        WHERE fk_leitor_email = %s""", (current_user[0],))
        your_lists = cursor.fetchall()

        t = PrettyTable(['Opção','Nome', 'Tags', 'Livros'])#cabecario da tabela

        for lista in your_lists:
            cursor.execute("""SELECT tagl FROM lista
                              JOIN posse_tagl ON (lista.codlista = posse_tagl.fk_lista_codlista)
                              JOIN tag_lista ON (posse_tagl.fk_tag_lista_codtagl = tag_lista.codtagl)
                              WHERE fk_leitor_email = %s AND lista.nome = %s
                              """, (current_user[0], lista[0],))
            your_tagls = cursor.fetchall()

            cursor.execute("""SELECT livro.titulo FROM lista
                              JOIN contem ON (lista.codlista = contem.fk_lista_codlista)
                              JOIN livro ON (contem.fk_livro_isbn= livro.isbn)
                              WHERE fk_leitor_email = %s AND lista.nome = %s""", (current_user[0],lista[0],))
            livros = cursor.fetchall()

            pretty_books = ''#Printa os livros mais bonitos
            for livro in livros:
                pretty_books += str(livro[0]) + new_line

            pretty_tags = '' #Printa mais bonitos a tag
            for tag in your_tagls:

                pretty_tags += '#'
                pretty_tags += str(tag[0]) + ', '#adiciona o newline com a tag

            t.add_row([str(counter_lists), lista[0], str(pretty_tags), str(pretty_books)])
            counter_lists += 1

        print(t) #Printa lista

        while True:
            msg = "Voce gostaria de:" + new_line
            new = "[1] Criar uma nova lista" + new_line
            edit = "[2] Editar uma lista" + new_line
            quit = "[3] Voltar" + new_line + '>>'

            msg += new + edit + quit

            section = input(msg)

            if section == '1':
                create_new_list(current_user, conn, cursor)
            elif section == '2':
                codlista = choose_lists(your_lists)
                edit_lists_menu(codlista, conn, cursor)
            elif section == '3':
                logged = False
                break
            else:
                continue
            os.system('clear')

def lists_page(current_user):
    """ Implements page of lists """

    # Connect to the database
    conn = psycopg2.connect(host='127.0.0.1',
                            password='12345',
                            user='postgres',
                            dbname='GOODREADS')
    logged = True

    while(logged):
        newline = '\n'
        msg = "Selecione quais listas você gostaria de ver:" + newline
        name_lists = '[1] Procurar uma lista pelo nome' + newline
        tag_lists = '[2] Procurar uma lista pela tag' + newline
        your_lists = '[3] Suas listas' + newline
        quit = '[4] Voltar ao menu inicial' + newline + ">>"

        msg += name_lists
        msg += tag_lists
        msg += your_lists
        msg += quit

        section = input(msg)

        cur = conn.cursor()

        if section == '1':
            search_by_name(10, cur)
        elif section == '2':
            search_by_tag(10, cur)
        elif section == '3':
            show_your_lists(10, current_user, conn, cur)
        else:
            logged = False
        os.system('clear')

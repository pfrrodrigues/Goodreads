import psycopg2  # Module to connect to the database
import os        # Auxiliar module to use unix commands
from passlib.hash import pbkdf2_sha256 # Module to obtain hash for passwords
import home as hm
from prettytable import PrettyTable

new_line = "\n"

def get_fav_genero(cursor, email):
    generos = ''
    
    os.system('clear')

    cursor.execute(""" SELECT  leitor.email, genero.nome, COUNT(livro.isbn)
                        FROM leitor
                        JOIN leitura ON (leitor.email = leitura.fk_leitor_email)
                        JOIN livro ON (livro.isbn = leitura.fk_livro_isbn)
                        JOIN posse_genero ON (livro.isbn = posse_genero.fk_livro_isbn)
                        JOIN genero ON(genero.codgenero = posse_genero.fk_genero_codgenero)
                        GROUP BY leitor.email, genero.nome
                        HAVING (leitor.email, COUNT (leitura.fk_livro_isbn)) IN
                        (SELECT le, MAX(cntisbn)
                        FROM (SELECT leitor.email le, genero.nome gen, COUNT(leitura.fk_livro_isbn) cntisbn
                            FROM leitor
                            JOIN leitura ON (leitor.email = leitura.fk_leitor_email)
                            JOIN livro ON (livro.isbn = leitura.fk_livro_isbn)
                            JOIN posse_genero ON (livro.isbn = posse_genero.fk_livro_isbn)
                            JOIN genero ON(genero.codgenero = posse_genero.fk_genero_codgenero)
                            GROUP BY leitor.email, genero.nome
                            HAVING leitor.email = %s)cnt
                        GROUP BY le); """, (email,))
    generos_temp  = cursor.fetchall()

    for gen in generos_temp:
        generos += gen[1]

    return generos

def get_top_10(cursor):
    autores = ''
    os.system('clear')
    cursor.execute("SELECT * FROM show_most_read")
    aut_temp = cursor.fetchall()

    cnt = 1
    for aut in aut_temp:
        autores += str(cnt) + ". " + aut[0] + " com " + str(aut[1]) +  " Leituras" + "\n"
        cnt += 1

    return autores

def print_autor_livro(cursor):

    t = PrettyTable(['Autor', 'Titulo'])#cabecario da tabela

    os.system('clear')

    cursor.execute(""" SELECT leitor.nome, livro.titulo, COUNT(livro.isbn)
                        FROM leitor
                        JOIN escrita ON (fk_leitor_email = email)
                        JOIN livro ON(escrita.fk_livro_isbn = isbn)
                        JOIN leitura ON (isbn = leitura.fk_livro_isbn)
                        GROUP BY leitor.email, livro.isbn
                        HAVING (leitor.email , COUNT(leitura.fk_livro_isbn)) IN
                            (SELECT le, MAX(cntisbn)
                            FROM (SELECT leitor.email le, COUNT (leitura.fk_livro_isbn) cntisbn
                                FROM leitor
                                JOIN escrita ON (fk_leitor_email = email)
                                JOIN livro ON(escrita.fk_livro_isbn = isbn)
                                JOIN leitura ON (isbn = leitura.fk_livro_isbn)
                                GROUP BY leitor.email,livro.isbn) cnt
                            GROUP BY le); """)
    books = cursor.fetchall()

    for book in books:
        t.add_row([book[0], book[1]])

    print(t)

def stats_page(userdata):
    """ Imprime as paginas de estatísticas"""


    conn = psycopg2.connect(host='127.0.0.1',
                            password='12345',
                            user='postgres',
                            dbname='actual')

    cursor = conn.cursor()

    menu = True
    msg = "Digite o que ver:" + new_line
    gen = "[1] Seu(s) gêneros favoritos" + new_line
    top = "[2] Top 10 Autores" + new_line
    livros = "[3] Livros mais lidos de cada Autor" + new_line
    quit = "[q] Voltar" +  new_line + ">>"

    msg += gen + top + livros + quit

    fav_genero = get_fav_genero(cursor, userdata[0])
    genero = "Seu(s) gênero(s) favoritos são: " + fav_genero

    top_10_autores = get_top_10(cursor)
    top_10 = "Os top 10 Autores são :" + new_line +  top_10_autores

    while menu:
        os.system('clear')
        opt = input(msg)
        if opt == '1':
            print(genero)
            input()
        elif opt == '2':
            print(top_10)
            input()
        elif opt == '3':
            print_autor_livro(cursor)
            input()
        elif opt == 'q':
            menu = False
        else:
            print("Comando Inválido" + new_line)

    # Close connection with the database
    cursor.close()
    conn.close()

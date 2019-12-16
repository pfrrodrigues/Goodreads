#  File:
#        searchbooks.py
#
#  Module:
#        searchbooks
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

def mark_book(email, isbn):

        # Connect to the database
        conn = psycopg2.connect(host='127.0.0.1',
                                password='12345',
                                user='postgres',
                                dbname='actual')
        # Create a cursor
        cur = conn.cursor()

        # Colects the extra information of the book
        cur.execute("SELECT * FROM info_book(%s)", (isbn,))
        book_information = cur.fetchall()

        # Get the average of the book
        cur.execute("SELECT * FROM avg_rating(%s);", (isbn,))
        avg_rating = cur.fetchone()

        # Case the book don't received a note yet
        if not avg_rating[0]:
            avg_rating = (0.00,)

        # Strucute of output table
        t = PrettyTable(['Título','Autor','Gênero', 'Ano de Publicação',
                         'Páginas','Formato', 'Media Nota'])

        print(book_information)

        t.add_row([book_information[0][1], book_information[0][7],
                   book_information[0][8], book_information[0][2],
                   book_information[0][5],book_information[0][6], "{:.2f}".format(avg_rating[0])])

        # Print the table with the book information
        print(t)

        while True:
            option = input("[1] Marcar livro\n[2] Ver descrição do livro\n[3] Voltar\n>> ")

            if int(option) < 1 or int(option) > 3:
                continue
            else:
                if option == '1':
                    while True:
                        marking = (input("[D/d] DESEJO LER\n[A/a] ATUALMENTE LENDO\n[L/l] LIDO\n>> ")).upper()

                        if marking == 'D':
                            cur.execute("SELECT isbn FROM marked(%s) WHERE isbn = %s;", (email,isbn,))
                            is_my_book = cur.fetchone()

                            if is_my_book:
                                print("Livro já está pertence a sua lista de livros. Vá até 'Meus Livros' e selecione 'Alterar marcação do livro.'")
                                break
                            else:
                                cur.execute("INSERT INTO leitura VALUES(%s,%s,'D',NULL);", (email, isbn))
                                conn.commit()
                                print("Livro adicionado a sua lista de livros.")
                                break
                        elif marking == 'A':
                            cur.execute("SELECT isbn FROM marked(%s) WHERE isbn = %s;", (email,isbn,))
                            is_my_book = cur.fetchone()

                            if is_my_book:
                                print("Livro já está pertence a sua lista de livros. Vá até 'Meus Livros' e selecione 'Alterar marcação do livro.'")
                                break
                            else:
                                cur.execute("INSERT INTO leitura VALUES(%s,%s,'D',NULL);", (email, isbn,))
                                conn.commit()
                                print("Livro adicionado a sua lista de livros.")
                                break
                        elif marking == 'L':
                            cur.execute("SELECT isbn FROM marked(%s) WHERE isbn = %s;", (email,isbn,))
                            is_my_book = cur.fetchone()

                            if is_my_book:
                                print("Livro já está pertence a sua lista de livros. Vá até 'Meus Livros' e selecione 'Alterar marcação do livro.'")
                                break
                            else:
                                while True:
                                    nota = int(input("Dê uma classificação para o livro[0-5]: "))
                                    if nota < 0 or nota > 5:
                                        continue
                                    else:
                                        cur.execute("INSERT INTO leitura VALUES(%s,%s,'L',%s);", (email, isbn, nota,))
                                        conn.commit()
                                        print("Livro adicionado a sua lista de livros.")
                                        break
                                break
                        else:
                            continue
                    break
                elif option == '2':
                    print('\n' + book_information[0][3] + '\n')
                else: # return
                    break

        # Close connection with the database
        cur.close()
        conn.close()




def searchbooks_page(email):
    """  """

    # Connect to the database
    conn = psycopg2.connect(host='127.0.0.1',
                            password='12345',
                            user='postgres',
                            dbname='actual')
    # Create a cursor
    cur = conn.cursor()

    while True:
        counter_books = 1

        option = input("[1] Pesquisa Geral\n[2] Pesquisar livro por autor\n[3] Pesquisar livro por gênero\n[4] Voltar\n>> ")

        if option == '1':
            book = (input("Digite o nome do livro: ")).title()
            cur.execute("SELECT isbn, titulo FROM livro WHERE titulo LIKE %s", (book+'%',))
            books = cur.fetchall()

            if books:
                table = PrettyTable(['Código', 'ISBN', 'Titulo'])
                if len(books) > 1:
                    for i in range(len(books)):
                        table.add_row([counter_books,books[i][0], books[i][1]])
                        counter_books += 1
                else:
                    table.add_row([counter_books, books[0][0], books[0][1]])
                    counter_books += 1

                print(table)

                while True:
                    opt = input("Digite código do livro para ver mais informações\n["+str(counter_books)+"] Voltar\n>> ")

                    if int(opt) > 0 and int(opt) < counter_books :
                        mark_book(email, books[int(opt)-1][0])
                    elif int(opt) == counter_books:
                        break
                    else:
                        continue
            else:
                print("Desculpe, não achamos o seu livro no catálogo.")

        elif option == '2':
            author = (input("Digite o nome do autor: ")).title()
            cur.execute("SELECT * FROM search_author_books(%s);", (author,))
            books = cur.fetchall()

            if books:
                table = PrettyTable(['Código', 'ISBN', 'Titulo'])
                if len(books) > 1:
                    for i in range(len(books)):
                        table.add_row([counter_books,books[i][0], books[i][1]])
                        counter_books += 1
                else:
                    table.add_row([counter_books, books[0][0], books[0][1]])
                    counter_books += 1

                print(table)

                while True:
                    opt = input("Digite código do livro para ver mais informações\n["+str(counter_books)+"] Voltar\n>> ")

                    if int(opt) > 0 and int(opt) < counter_books :
                        mark_book(email, books[int(opt)-1][0])
                    elif int(opt) == counter_books:
                        break
                    else:
                        continue
            else:
                print("Desculpe, não achamos os livros do autor.")


        elif option == '3':
            genre = (input("Digite o gênero de sua escolha: ")).title()
            cur.execute("SELECT * FROM search_for_gen(%s)", (genre,))
            books = cur.fetchall()

            if books:
                table = PrettyTable(['Código', 'ISBN', 'Titulo'])
                if len(books) > 1:
                    for i in range(len(books)):
                        table.add_row([counter_books,books[i][0], books[i][1]])
                        counter_books += 1
                else:
                    table.add_row([counter_books, books[0][0], books[0][1]])
                    counter_books += 1

                print(table)

                while True:
                    opt = input("Digite código do livro para ver mais informações\n["+str(counter_books)+"] Voltar\n>> ")

                    if int(opt) > 0 and int(opt) < counter_books :
                        mark_book(email, books[int(opt)-1][0])
                    elif int(opt) == counter_books:
                        break
                    else:
                        continue
            else:
                print("Desculpe, não encontramos os livros do gênero fornecido.")

        elif option == '4':
            break
        else:
            continue

    # Close the connection with the database
    cur.close()
    conn.close()

#  File:
#        mybooks.py
#
#  Module:
#        mybooks
#
#  Authors: Arthur Camargo and Pablo Rodrigues
#
#  Description:
#
##############################################################################
#  Create Date: 12.12.2019
#
#  Last Modified Date:
#       12.12.2019
#
#  Additional Comments:
##############################################################################
import psycopg2
import os
from prettytable import PrettyTable


def select_book(email, book):
    """ Description """

    # Connect to the database
    conn = psycopg2.connect(host='127.0.0.1',
                            password='12345',
                            user='postgres',
                            dbname='actual')
    # Create a cursor
    cur = conn.cursor()


    # Variables
    description = "[1] Ver descrição do livro"
    marking = "[2] Alterar marcação do livro"
    rtrn = "[3] Voltar"


    # Colects the extra information of the book
    cur.execute("SELECT * FROM info_book(%s)", (book[0],))
    book_information = cur.fetchall()

    # Get the average of the book
    cur.execute("SELECT * FROM avg_rating(%s);", (book[0],))
    avg_rating = cur.fetchone()

    # Case the book don't received a note yet
    if not avg_rating[0]:
        avg_rating = (0.00,)

    # Strucute of output table
    t = PrettyTable(['Título','Autor','Gênero', 'Ano de Publicação',
                     'Páginas','Formato', 'Nota', 'Media Nota', 'Tipo'])


    # Type book treatment(currently reading or wish to read)
    if book[4] == 'D' or book[4] == 'A':
        if len(book_information) == 1:
            t.add_row([book_information[0][1], book_information[0][7],
                      book_information[0][8], book_information[0][2],
                       book_information[0][5], book_information[0][6],' ', "{:.2f}".format(avg_rating[0]), book[4]])
        else:
            for i in range(len(book_information)):
                t.add_row([book_information[i][1], book_information[i][7],
                          book_information[i][8], book_information[i][2],
                           book_information[i][5], book_information[i][6],' ', "{:.2f}".format(avg_rating[0]), book[4]])

    # Type book treatment(read)
    else:
        if len(book_information) == 1:
            t.add_row([book_information[0][1], book_information[0][7],
                      book_information[0][8], book_information[0][2],
                       book_information[0][5], book_information[0][6],book[5], "{:.2f}".format(avg_rating[0]), book[4]])
        else:
            for i in range(len(book_information)):
                t.add_row([book_information[i][1], book_information[i][7],
                          book_information[i][8], book_information[i][2],
                           book_information[i][5], book_information[i][6],book[5], "{:.2f}".format(avg_rating[0]), book[4]])

    # Print the table with the book information
    print(t)

    while True:
        option = input(description+'\n'+marking+'\n'+rtrn+'\n>> ')

        if int(option) < 1 or int(option) > 3:
            option = input(description+'\n'+marking+'\n'+rtrn+'\n>> ')
        else:
            # Print description
            if option == '1':
                print('\n' + book_information[0][3] + '\n')

            # Changes de type
            elif option == '2':
                if book[4] == 'D':
                    while True:
                        type = (input("\nMarcar livro como:\n  [L/l] LIDO\n  [A/a] ATUALMENTO LENDO\n>> ")).upper()

                        if type == 'L':
                            while True:
                                classification = input("Classificação do livro[0-5]: ")

                                if int(classification) < 0 or int(classification) > 5:
                                    continue
                                else:
                                    cur.execute("UPDATE leitura SET tipo='L', classificacao=%s WHERE fk_leitor_email=%s and fk_livro_isbn=%s",
                                    (str(int(classification)),email,book[0],))
                                    conn.commit()
                                    break
                            break
                        elif type == 'A':
                            cur.execute("UPDATE leitura SET tipo = 'A' WHERE fk_leitor_email=%s and fk_livro_isbn=%s",
                            (email,book[0],))
                            conn.commit()
                            break
                        else:
                            continue

                elif book[4] == 'A':
                    while True:
                        type = (input("\nMarcar livro como:\n  [L/l] LIDO\n  [D/d]DESEJO LER\n>> ")).upper()

                        if type == 'D':
                            cur.execute("UPDATE leitura SET tipo = 'D' WHERE fk_leitor_email=%s and fk_livro_isbn=%s;",
                            (email,book[0],))
                            conn.commit()
                            break
                        elif type == 'L':
                            while True:
                                classification = input("Classificação do livro[0-5]: ")

                                if int(classification) < 0 or int(classification) > 5:
                                    continue
                                else:
                                    cur.execute("UPDATE leitura SET tipo='L', classificacao=%s WHERE fk_leitor_email=%s and fk_livro_isbn=%s",
                                    (str(int(classification)),email,book[0],))
                                    conn.commit()
                                    break
                            break
                else:
                    type = (input("\nMarcar livro como:\n  [A/a] ATUALMENTE LENDO\n  [D/d]DESEJO LER\n>> ")).upper()

                    while True:
                        if type == 'D':
                            cur.execute("UPDATE leitura SET tipo = 'D', classificacao = 0 WHERE fk_leitor_email=%s and fk_livro_isbn=%s;",
                            (email,book[0],))
                            conn.commit()
                            break
                        elif type == 'A':
                            cur.execute("UPDATE leitura SET tipo = 'A', classificacao = 0 WHERE fk_leitor_email=%s and fk_livro_isbn=%s;",
                            (email,book[0],))
                            conn.commit()
                            break
            # Comeback
            else:
                break


    # Close the connection with the database
    conn.close()
    cur.close()



def mybooks_page(email):
    """  """

    # Connect to the database
    conn = psycopg2.connect(host='127.0.0.1',
                            password='12345',
                            user='postgres',
                            dbname='actual')
    # Create a cursor
    cur = conn.cursor()

    msg_info_books = "Para ver mais informacoes de um de seus livros entre com seu codigo de selecao correspondente."
    msg_return = "Voltar."
    processing = True

    while processing:
        counter_books = 1

        os.system('clear')

        # Obtain the marked books of user
        cur.execute("SELECT * FROM marked(%s);", (email,))
        books = cur.fetchall()

        if books:
            t = PrettyTable(['Opção','Título','Autor','Tipo', 'Nota', 'Nota Media'])

            for book in books:

                # Get the average of the book
                cur.execute("SELECT * FROM avg_rating(%s);", (book[0],))
                avg_rating = cur.fetchone()

                # Case the book don't received a note yet
                if not avg_rating[0]:
                    avg_rating = (0.00,)

                if book[4] == 'D':
                    t.add_row([str(counter_books), book[1], book[3], book[4], ' ', "{:.2f}".format(avg_rating[0])])
                elif book[4] == 'A':
                    t.add_row([str(counter_books), book[1], book[3], book[4], ' ', "{:.2f}".format(avg_rating[0])])
                else:
                    t.add_row([str(counter_books), book[1], book[3], book[4], book[5], "{:.2f}".format(avg_rating[0])])
                counter_books += 1


            # Print the table with the books
            print(t)

            # Check the options
            option = input('\n' + msg_info_books + '\n\n' + str(counter_books) + '. ' + msg_return + '\n>> ')
            option = int(option)

            # signifca que e o codigo de um dos livros
            if option > 0 and option < counter_books:
                select_book(email, books[option-1])

            #significa que e a opcao de voltar
            elif option == counter_books:
                processing = False
            # invalido
            else:
                continue
        else:
            print("Nenhum livro na lista.")

            option = input('\n\n' + str(counter_books) + '. ' + msg_return + '\n>> ')


    conn.close()
    cur.close()

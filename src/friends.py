#  File:
#        friends.py
#
#  Module:
#        friends
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


def add_friend(email):
    # Connect to the database
    conn = psycopg2.connect(host='127.0.0.1',
                            password='12345',
                            user='postgres',
                            dbname='actual')
    # Create a cursor
    cur = conn.cursor()

    # Clean the terminal
    os.system('clear')

    table = PrettyTable(['Opcao','Nome', 'Email'])

    processing_case = True
    while processing_case:
        counter_friends = 1

        # Print the case messages
        # name = 1, email = 2
        name_or_email = input("[1] Procurar por nome\n[2] Procurar por email\n>> ")

        if name_or_email != '1' and name_or_email != '2':
            continue
        else:
            # Search by name
            if name_or_email == '1':
                friend_name = (input("Digite o nome do amigo que você deseja buscar: ")).title()

                cur.execute("SELECT nome, email FROM leitor WHERE nome LIKE %s and email != %s;", (friend_name+'%',email,))
                new_friends = cur.fetchall()

                # If not find friends with that name...
                if not new_friends:
                    print("\nDesculpe, não encontramos usuário com nome semelhante.")
                    processing_case = False
                else:
                    for friend in new_friends:
                        table.add_row([str(counter_friends), friend[0], friend[1]])
                        counter_friends += 1
                    print(table)

                    while True:
                        option = input("Digite o número de opção correspondente se deseja adicioná-lo senão digite um comando.\n"+"["+str(counter_friends)+"] "+" Voltar\n>> ")

                        if int(option) < 1 or int(option) > counter_friends:
                            continue
                        else:
                            if int(option) == counter_friends:
                                break
                            else:
                                cur.execute("SELECT FK_Leitor_email_ FROM amizade WHERE FK_Leitor_email_ = %s", (new_friends[int(option)-1][1],))
                                is_friend = cur.fetchone()

                                if is_friend:
                                    print("Este usuário já está na sua lista de amigos.")
                                    break
                                else:
                                    cur.execute("INSERT INTO amizade VALUES(%s,%s);", (email, new_friends[int(option)-1][1],))
                                    conn.commit()

                                    cur.execute("SELECT FK_Leitor_email_ FROM amizade WHERE FK_Leitor_email_ = %s;", (new_friends[int(option)-1][1],))
                                    test_add = cur.fetchone()

                                    if test_add:
                                        print("Leitor adicionado na sua lista de amigos.")
                                        break
                                    else:
                                        print("Desculpe, houve um erro ao adicionar o leitor a sua lista de amigos.")
                                        break
                    processing_case = False

            # Search by email
            else:
                friend_email = input("Digite o email do amigo que você deseja buscar: ")

                cur.execute("SELECT nome, email FROM leitor WHERE email = %s and email != %s;", (friend_email,email,))
                new_friends = cur.fetchall()

                # If not find friends with that email...
                if not new_friends:
                    print("\nDesculpe, não encontramos usuário com email semelhante.")
                    processing_case = False
                else:
                    for friend in new_friends:
                        table.add_row([str(counter_friends), friend[0], friend[1]])
                        counter_friends += 1
                    print(table)

                    while True:
                        option = input("Digite o número de opção correspondente se deseja adicioná-lo senão digite um comando.\n"+"["+str(counter_friends)+"] "+" Voltar\n>> ")

                        if int(option) < 1 or int(option) > counter_friends:
                            continue
                        else:
                            if int(option) == counter_friends:
                                break
                            else:
                                cur.execute("SELECT FK_Leitor_email_ FROM amizade WHERE FK_Leitor_email_ = %s", (new_friends[int(option)-1][1],))
                                is_friend = cur.fetchone()

                                if is_friend:
                                    print("Este usuário já está na sua lista de amigos.")
                                    break
                                else:
                                    cur.execute("INSERT INTO amizade VALUES(%s,%s);", (email, new_friends[int(option)-1][1],))
                                    conn.commit()

                                    cur.execute("SELECT FK_Leitor_email_ FROM amizade WHERE FK_Leitor_email_ = %s;", (new_friends[int(option)-1][1],))
                                    test_add = cur.fetchone()

                                    if test_add:
                                        print("Leitor adicionado na sua lista de amigos.")
                                        break
                                    else:
                                        print("Desculpe, houve um erro ao adicionar o leitor a sua lista de amigos.")
                                        break
                    processing_case = False


    # Close connection with the database
    cur.close()
    conn.close()


def delete_friend(user_email, friend_email):
    # Connect to the database
    conn = psycopg2.connect(host='127.0.0.1',
                            password='12345',
                            user='postgres',
                            dbname='actual')
    # Create a cursor
    cur = conn.cursor()

    cur.execute("DELETE FROM amizade WHERE fk_Leitor_email = %s and fk_Leitor_email_ = %s", (user_email, friend_email,))
    conn.commit()

    print("Amigo removido da sua lista.")

    # Close the connection with the database
    cur.close()
    conn.close()


def see_friends_books(email):
    # Connect to the database
    conn = psycopg2.connect(host='127.0.0.1',
                            password='12345',
                            user='postgres',
                            dbname='actual')
    # Create a cursor
    cur = conn.cursor()

    # Obtain the marked books of user
    cur.execute("SELECT * FROM marked(%s);", (email,))
    books = cur.fetchall()

    if books:
        t = PrettyTable(['Título','Autor','Tipo', 'Nota', 'Nota Media'])

        list_of_books = []

        for book in books:
            if book[1] in list_of_books:
                continue

            # Get the average of the book
            cur.execute("SELECT * FROM avg_rating(%s);", (book[0],))
            avg_rating = cur.fetchone()

            # Case the book don't received a note yet
            if not avg_rating[0]:
                avg_rating = (0.00,)

            if book[4] == 'D':
                t.add_row([book[1], book[3], book[4], ' ', "{:.2f}".format(avg_rating[0])])
            elif book[4] == 'A':
                t.add_row([book[1], book[3], book[4], ' ', "{:.2f}".format(avg_rating[0])])
            else:
                t.add_row([ book[1], book[3], book[4], book[5], "{:.2f}".format(avg_rating[0])])
            list_of_books.append(book[1])

        # Print the table with the books
        print(t)
    else:
        print("Seu amigo não possui nenhum livro marcado.")


    # Close the connection
    cur.close()
    conn.close()


def friends_page(email):
    """"""

    # Connect to the database
    conn = psycopg2.connect(host='127.0.0.1',
                            password='12345',
                            user='postgres',
                            dbname='actual')
    # Create a cursor
    cur = conn.cursor()

    # Messages
    msg_add_friend = "Adicionar amigo"
    msg_delete_friend = "Excluir um amigo da lista"
    msg_see_books = "Ver livros marcados de seus amigos"
    msg_return = "Voltar"

    pressed_return = False
    while not pressed_return:
        counter_friends = 1

        # Takes the list of friends
        cur.execute("SELECT * FROM my_friends(%s);", (email,))
        friends = cur.fetchall()

        if friends:
            table = PrettyTable(['Opcao','Amigo', 'Email'])
            for friend in friends:
                table.add_row([str(counter_friends), friend[0], friend[1]])
                counter_friends+=1
            print(table)

            print('\n['+str(counter_friends)+'] ' + msg_add_friend+'\n')
            counter_friends += 1
            print('['+str(counter_friends)+'] ' + msg_delete_friend+'\n')
            counter_friends += 1
            print('['+str(counter_friends)+'] ' + msg_see_books+'\n')
            counter_friends += 1
            print('['+str(counter_friends)+'] ' + msg_return+'\n')

            option = input(">> ")

            if int(option) == (counter_friends-3):
                add_friend(email)
            elif int(option) == (counter_friends-2):
                while True:
                    rfriend = input("Digite o número da opção do amigo a ser deletado: ")
                    if int(rfriend) < 1 or int(rfriend) > (counter_friends-4):
                        continue
                    else:
                        delete_friend(email, friends[int(rfriend)-1][1])
                        break
            elif int(option) == (counter_friends-1):
                while True:
                    rfriend = input("Digite o número da opção do amigo no qual você desejar ver os livros: ")
                    if int(rfriend) < 1 or int(rfriend) > (counter_friends-4):
                        continue
                    else:
                        see_friends_books(friends[int(rfriend)-1][1])
                        break
            elif int(option) == (counter_friends):
                pressed_return = True
            else:
                continue

        else:
            print("Você ainda não possui nenhum amigo")

            print('\n['+str(counter_friends)+'] ' + msg_add_friend+'\n')
            counter_friends += 1

            print('['+str(counter_friends)+'] ' + msg_return+'\n')

            option = input(">> ")

            if int(option) == (counter_friends-1):
                add_friend(email)
            elif int(option) == (counter_friends):
                pressed_return = True
            else:
                continue

    # Close the connection with the database
    cur.close()
    conn.close()

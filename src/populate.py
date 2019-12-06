#  File:
#        populate.py
#
#  Module:
#        populate
#
#  Authors: Arthur Camargo and Pablo Rodrigues
#
#  Description: populate the tables of the database for the project of FDB
#
##############################################################################
#  Create Date: 06.12.2019
#
#  Last Modified Date:
#       06.12.2019
#
#  Additional Comments: 'books.csv' is a csv file downloaded of Kaggle
##############################################################################
from goodreads import client
import psycopg2
import csv

# Authentication client
gc = client.GoodreadsClient('iqyXQgwp5QTsbwZdK4xpPQ', '1SdWgKoZCOFDRWIZldacR9jGnkeagwhloZqoXRPqxRA')

# Conect to the database
conn = psycopg2.connect(host="127.0.0.1",
                        user="postgres",
                        password="12345",
                        dbname="test-goodreads",
                        port="5432")

# Open the cursor of db
cur = conn.cursor()

def populate_books():
    # Populates the book table in database
    filename = 'books.csv'
    isbns = []

    with open(filename) as f:
        reader = csv.reader(f, delimiter=',', skipinitialspace=True)
        header = next(reader)

        for row in reader:
            isbns.append(row[4])

        for i in range(10):
            isbn_book = isbns[i]
            book = gc.book(isbn=isbn_book)

            cur.execute("INSERT INTO Livro values(%s, %s, %s, %s, %s, %s, %s)",
            (book.isbn, book.title, book.description, book.num_pages, book.format,
             book.publication_date, book.image_url))


def populate_format():
    # Populates the format table in database




# Make the changes to the database persistent
conn.commit()

# Close the communication with the database
cur.close()
conn.close()

"""
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
#       05.12.2019
#
#  Additional Comments:
#
#
##############################################################################
"""
import psycopg2
from goodreads import client


KEY = 'iqyXQgwp5QTsbwZdK4xpPQ'
SECRET = '1SdWgKoZCOFDRWIZldacR9jGnkeagwhloZqoXRPqxRA'
GC = client.GoodreadsClient(KEY, SECRET)

BOOK = GC.book(2)

"""
print(BOOK.isbn)
print(BOOK.title)
print(BOOK.description)
print(BOOK.num_pages)
print(BOOK.image_url)
print(BOOK.publication_date)
"""

date = BOOK.publication_date
date = date[2] + '-' + date[1] + '-' + date[0]

# Connect to an existing database

conn = psycopg2.connect(dbname="goodreads", user="postgres")

# Open a cursor to perform database operations
cur = conn.cursor()

cur.execute(
    """
    INSERT INTO livro(isbn, titulo)
    VALUES (%s,%s);
    """,
    (BOOK.isbn, BOOK.title)
)

cur.execute(
        """
        SELECT * FROM livro;
    """
)

query_test = cur.fetchall()

for instance in query_test:
    print(instance)

# Close communication with the database
cur.close()
conn.close()

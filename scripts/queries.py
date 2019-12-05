""" Goodreads useful queries """
from goodreads import client

KEY = 'iqyXQgwp5QTsbwZdK4xpPQ'
SECRET = '1SdWgKoZCOFDRWIZldacR9jGnkeagwhloZqoXRPqxRA'
GC = client.GoodreadsClient(KEY, SECRET)

BOOK = GC.book(12)

print(BOOK.title)
print(BOOK.authors)

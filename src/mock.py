""" Modules for mocking the goodreads database """

import psycopg2

def insert(table, *parameters):
    """ fuction to insert attributes to the database"""

    Query1 = "INSERT INTO" + table + "("
    for i in range(len(parameters)/2):
        #just half of the parameters

        Query1 = Query1 + parameters[i] + ", "

    Query2 = ") VALUES ( "

    for i in range(len(parameters)/2, len(parameters)):

        Query2 = Query2 + parameters[i] + ", "

    Query2 = Query2 + ");"

    Query = Query1 + Query2

    return Query

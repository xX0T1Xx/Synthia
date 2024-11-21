import sqlite3

def run(query, params=[]):
    connection = sqlite3.connect('data/database.db')
    cursor = connection.cursor()
    cursor.execute(query, params)
    connection.commit()
    cursor.close()

def run_many(query, params=[]):
    connection = sqlite3.connect('data/database.db')
    cursor = connection.cursor()
    cursor.executemany(query, params)
    connection.commit()
    cursor.close()

def fetch(query, params=[]):
    connection = sqlite3.connect('data/database.db')
    cursor = connection.cursor()
    cursor.execute(query, params)
    return cursor.fetchall()

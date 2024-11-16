import sqlite3
import os

connection = sqlite3.connect('answers.db')
cursor = connection.cursor()

def createData():
    if not os.path.exists('answers.db'):
        cursor.execute('''
            CREATE TABLE answers (
                id      INTEGER PRIMARY KEY
                                UNIQUE
                                NOT NULL,
                value   INTEGER
            );''')
        connection.commit()

def fetchData():
    cursor.execute("SELECT value FROM answers")
    data = cursor.fetchall()
    
    return data
    
def deleteData(value):
    query = "DELETE FROM answers WHERE value = ?"
    cursor.execute(query, (value,))
    connection.commit()
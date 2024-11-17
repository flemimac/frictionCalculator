import sqlite3
import os

connection = sqlite3.connect('results.db')
cursor = connection.cursor()

def createData():
    if not os.path.exists('results.db'):
        cursor.execute('''
            CREATE TABLE answers (
                id      INTEGER PRIMARY KEY
                                UNIQUE
                                NOT NULL,
                value   INTEGER
            );''')
        connection.commit()

def fetchData():
    cursor.execute("SELECT id, value FROM answers")
    data = cursor.fetchall()
    
    return data
    
def deleteData(number):
    query = "DELETE FROM answers WHERE id = ?"
    cursor.execute(query, (number,))
    connection.commit()
    
def addData(value):
    query = f"INSERT INTO answers (value) VALUES (?)"
    cursor.execute(query, (value,))
    connection.commit()
    
def clearData():
    cursor.execute("DELETE FROM answers")
    connection.commit()
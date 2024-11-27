import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

def createData():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS answers (
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
    
def allData():
    cursor.execute("SELECT value FROM answers")
    values = cursor.fetchall()
    
    return [value[0] for value in values] 

def saveData():
    cursor.execute("SELECT id, value FROM answers")
    results = cursor.fetchall()
    
    return results
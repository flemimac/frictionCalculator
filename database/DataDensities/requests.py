import sqlite3
import os

connection = sqlite3.connect('densities.db')
cursor = connection.cursor()

def createData():
    if not os.path.exists('densities.db'):
        cursor.execute('''
            CREATE TABLE densities (
                id      INTEGER PRIMARY KEY
                                UNIQUE
                                NOT NULL,
                density TEXT,
                value   INTEGER
            );''')
        connection.commit()

def fetchData():
    cursor.execute("SELECT density, value FROM densities")
    data = cursor.fetchall()
    
    return data

def addData(density, value):
    query = f"INSERT INTO densities (density, value) VALUES (?, ?)"
    cursor.execute(query, (density, value))
    connection.commit()
    
def deleteData(density, value):
    query = "DELETE FROM densities WHERE density = ? AND value = ?"
    cursor.execute(query, (density, value))
    connection.commit()
    
def updateData(old_density, new_density, new_value):
    query = "UPDATE densities SET density = ?, value = ? WHERE density = ?"
    cursor.execute(query, (new_density, new_value, old_density))
    connection.commit()
    
def fetchMaterials(material):
    cursor.execute("SELECT value FROM densities WHERE density=?", (material,))
    result = cursor.fetchone()
    
    return result[0]
    
def loadMaterials(combo_box):
    cursor.execute("SELECT density FROM densities")
    materials = cursor.fetchall()

    for material in materials:
        combo_box.addItem(material[0])
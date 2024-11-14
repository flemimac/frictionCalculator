import sqlite3

connection = sqlite3.connect('densities.db')
cursor = connection.cursor()
    
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

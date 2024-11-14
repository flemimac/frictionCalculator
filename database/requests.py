import sqlite3

def fetch_data():
    connection = sqlite3.connect('densities.db')
    cursor = connection.cursor()
    
    cursor.execute("SELECT density, value FROM densities")
    data = cursor.fetchall()
    
    connection.close()
    
    return data
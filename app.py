import sqlite3

conn = sqlite3.connect('database.db')
print("Database connected successfully")

#Create a table if it doesn't exist
conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        address TEXT,
        city TEXT,
        pin TEXT)
""")
             
print("Table created successfully")
conn.close()

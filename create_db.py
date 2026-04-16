import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
id TEXT,
name TEXT,
attendance TEXT,
fees TEXT,
course TEXT,
photo TEXT
)
""")

connection.commit()

connection.close()

print("Database created successfully")

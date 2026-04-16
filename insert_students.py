import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

cursor.execute("""
INSERT INTO students VALUES (
'23D01019126',
'SHAIK KALVA SOHEB',
'89%',
'14000 pending',
'BCA',
'soheb.jpeg'
)
""")

connection.commit()

connection.close()

print("Student inserted successfully")

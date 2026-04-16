import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

cursor.execute("""
UPDATE students
SET photo='soheb.jpeg'
WHERE id='23D01019126'
""")

connection.commit()
connection.close()

print("Photo updated")

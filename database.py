import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id TEXT PRIMARY KEY,
name TEXT,
attendance TEXT,
fees TEXT,
course TEXT,
PHOTO TEXT
)
""")

cursor.execute("""
INSERT OR IGNORE INTO students VALUES
('23D01019126','SHAIK KALVA SOHEB','89%','14000 pending','BCA',soheb.jpeg),
('23D01019125','SHAIK JABIVULLA','85%','14000 pending','BCA',jabi.jpeg)
""")

connection.commit()

connection.close()

print("Database created successfully")

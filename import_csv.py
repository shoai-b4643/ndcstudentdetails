import csv
import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

with open("students.csv","r") as file:

    reader = csv.reader(file)

    next(reader)   # skip header row

    for row in reader:

        cursor.execute("""
        INSERT INTO students
        VALUES (?,?,?,?,?,?)
        """,row)

connection.commit()
connection.close()

print("All students inserted successfully")

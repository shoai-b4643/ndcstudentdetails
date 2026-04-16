from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():

    if request.method == 'POST':

        student_id = request.form['student_id']
        password = request.form['password']

        connection = sqlite3.connect("students.db")

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))

        data = cursor.fetchone()

        connection.close()

        if data:

            student = {
                "name": data[1],
                "attendance": data[2],
                "fees": data[3],
                "course": data[4],
                "photo": data[5]
            }

            return render_template("dashboard.html", student=student)

        else:
            return "Student not found"

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)

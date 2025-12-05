from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# Style
# @app.route('/static/<path:path>')
# def static_files(path):
#     return app.send_static_file(path)

DB_PATH = "database/database.db"

@app.route('/enternew')
def new_student():
    return render_template('student.html') 


@app.route('/addrec', methods=['POST'])
def add_rec():
    msg = ""
    con = None
    if request.method == 'POST':
        try:
            name = request.form['name']
            address = request.form['address']
            city = request.form['city']
            pin = request.form['pincode']

            con = sql.connect(DB_PATH)
            cur = con.cursor()
            cur.execute(
                "INSERT INTO students (name, address, city, pin) VALUES (?, ?, ?, ?)",
                (name, address, city, pin),
            )
            con.commit()
            msg = "Record successfully added"
        except Exception as e:
            if con:
                con.rollback()
            msg = f"Error in insert operation: {e}"
        finally:
            if con:
                con.close()
    return render_template("result.html", msg=msg)

        
@app.route('/list')
def list_records():
    con = sql.connect(DB_PATH)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    con.close()
    return render_template("list.html", rows=rows)



# New route for Edit
@app.route('/edit')
def edit_student():
    student_id = request.args.get('student_id', type=int)
    if not student_id:
        # if no one record was selected, it returns to the list
        return redirect(url_for('list_records'))

    con = sql.connect(DB_PATH)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cur.fetchone()
    con.close()

    if student is None:
        return redirect(url_for('list_records'))

    # send the record to the template
    return render_template("editStudent.html", student=student)

# update records
@app.route('/update', methods=['POST'])
def update_student():
    student_id = request.form['ID']
    name = request.form['name']
    address = request.form['address']
    city = request.form['city']
    pincode = request.form['pincode']

    con = sql.connect(DB_PATH)
    cur = con.cursor()
    cur.execute(
        "UPDATE students SET name = ?, address = ?, city = ?, pin = ? WHERE id = ?",
        (name, address, city, pincode, student_id),
    )
    con.commit()
    con.close()
    return redirect(url_for('list_records'))


@app.route('/delete')
def delete_student():
    student_id = request.args.get('student_id', type=int)
    if not student_id:
        return redirect(url_for('list_records'))

    con = sql.connect("database/database.db")
    cur = con.cursor()
    cur.execute("DELETE FROM students WHERE id = ?", (student_id,))
    con.commit()
    con.close()

    return redirect(url_for('list_records'))

if __name__ == '__main__':
    app.run(debug=True)
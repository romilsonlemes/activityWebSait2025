from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# Style
# @app.route('/static/<path:path>')
# def static_files(path):
#     return app.send_static_file(path)

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

            con = sql.connect('database.db')
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
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    con.close()
    return render_template("list.html", rows=rows)



# New route for Edit

@app.route('/edit')
def edit_student():
    # tablerow
    # msg = ""
    # con = None
    # if request.method == 'POST':
    #     try:    
    return render_template("editStudent.html") #, tablerow=tablerow)
    # return "Edit page coming soon!"

if __name__ == '__main__':
    app.run(debug=True)
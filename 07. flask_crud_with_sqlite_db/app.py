from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
import sqlite3 as sql
import os

@app.route("/")
def home_page():
    message = request.args.get("message")
    # fetching records 
    db_path = os.path.join(os.path.dirname(__file__), "database.db")
    with sql.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM `users`")
        records = cur.fetchall()
    return render_template("index.html", message=message, records=records)

@app.route("/addrecord", methods = ["POST", "GET"])
def add_record():
    if request.method == "POST":
        message = None
        con = None
        try:
            name = request.form["name"]
            email = request.form["email"]
            address = request.form["address"]
            database_path = os.path.join(os.path.dirname(__file__), "database.db")
            with sql.connect(database_path) as con:
                cur = con.cursor()
                cur.execute("INSERT INTO `users` (name, email, address) VALUES(?, ?, ?)", (name, email, address))
                con.commit()
                message = "Inserted Successfully"
        except Exception as e:
            con.rollback()
            message = f"Error While Inserting Data: {str(e)}"
        finally:
            con.close()
            return redirect(url_for("home_page", message=message))

# edit record 
@app.route("/edit", methods = ["GET", "POST"])
def edit_record():
    if request.method == "GET":
        record_id = request.args.get("id")
        if record_id:
            message = request.args.get("message")
            db_path = os.path.join(os.path.dirname(__file__), "database.db")
            with sql.connect(db_path) as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM `users` WHERE id=?", (record_id,))
                record = cur.fetchone()
            if record:
                return render_template("edit.html", record=record, message=message)
            else:
                return redirect(url_for("home_page"))
    elif request.method == "POST":
        # con = None
        try:
            record_id = request.form["id"]
            name = request.form["name"]
            email = request.form["email"]
            address = request.form["address"]

            db_path = os.path.join(os.path.dirname(__file__), "database.db")
            with sql.connect(db_path) as con:
                cur = con.cursor()
                cur.execute("UPDATE `users` SET name=?, email=?, address=? WHERE id=?", (name, email, address, record_id))
                con.commit()
                message = "Data Updated Successfully"
            return redirect(url_for("home_page", message="Data Updated Successfully"))
        except Exception as e:
            # con.rollback()
            message = str(e)
        finally:
            return redirect(url_for("home_page"))

# delete record 
@app.route("/del", methods = ["GET", "POST"])
def del_record():
    if request.method == "GET":
        record_id = request.args.get("id")
        if record_id:
            db_path = os.path.join(os.path.dirname(__file__), "database.db")
            with sql.connect(db_path) as con:
                cur = con.cursor()
                cur.execute("DELETE FROM `users` WHERE id=?",(record_id,))
                con.commit()
            return redirect(url_for("home_page"))




if __name__ == "__main__":
    app.run(debug=True)

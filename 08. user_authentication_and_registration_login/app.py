from flask import Flask, request, render_template, redirect, url_for, session
import os
import sqlite3 as sql
from datetime import datetime

# current time 
current_time = datetime.now()

# db path 
db_path = os.path.join(os.path.dirname(__file__), "database.db")
app = Flask(__name__)

# secret key 
app.secret_key = 'your_secret_key'

# profile page 
@app.route("/profile")
def profile_page():
    if "email" in session:
        with sql.connect(db_path) as con:
            email = session["email"]
            cur = con.cursor()
            cur.execute("SELECT * FROM `users` WHERE email=?", (email,))
            user = cur.fetchone()
            if user:
                email = user[2]
                name = user[1]
                created_date = user[4]
                return render_template("profile.html", name=name, email=email, date=created_date)
            else:
                return redirect(url_for("login"))
    else:
        return redirect(url_for("login"))

# home page 
@app.route("/")
def home_page():
    if not "email" in session:
        return render_template("index.html")
    else:
        return redirect(url_for("profile_page"))

# login 
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        with sql.connect(db_path) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM `users` WHERE `email`=? AND `password`=?",(email, password))
            user = cur.fetchone()
            if user:
                session["email"] = email
                alert_message = f"alert('You have Logged in');"
                return redirect(url_for("profile_page"))
            else:
                alert_message = f"alert('Email or Password Wrong');"
                return render_template("index.html", alert_message=alert_message)
    else:
        return render_template("index.html")  

# signup 
@app.route("/signup", methods = ["GET", "POST"])
def signup_page():
    if request.method == "GET":
        return render_template("signup.html")
    elif request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        
        # check existing email 
        with sql.connect(db_path) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM `users` WHERE `email`=?", (email,))
            user_find = cur.fetchone()
            if user_find:
                alert_message = f"alert('Your Email ID is Already Exist');"
                return render_template("signup.html", alert_message=alert_message)
            else:
                with sql.connect(db_path) as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO `users` (name, email, password, date) VALUES(?, ?, ?, ?)", (name, email, password, current_time))
                    con.commit()
                    alert_message = f"alert('You have Created Account Successfully Please Login Now');"
                return redirect(url_for("login", alert_message=alert_message))


# logout 
@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("email", None)
    return redirect(url_for("home_page"))    


if __name__ == "__main__":
    app.run(debug=True)

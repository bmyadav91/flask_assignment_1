# 5. Implement user sessions in a Flask app to store and display user-specific data.
from flask import Flask, render_template, redirect, session, g, url_for, request
app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route("/", methods = ["POST", "GET"])
def home_page():
    if 'userdata' in session:
        return f"{session['userdata']} <a href='/logout'>Logout</a>"
    
    else:
        if request.method == "POST":
            user_data = request.form["datasession"]
            session['userdata'] = user_data
            return redirect(url_for("home_page"))
        else:
            return render_template("index.html")

@app.route("/logout")
def flush_session():
    session.pop('userdata', None)
    return redirect(url_for("home_page"))

if __name__ == "__main__":
    app.run(debug=True)
# 4. Create a Flask app with a form that accepts user input and displays it.
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/result", methods = ["POST"])
def result():
    result = request.form.get("user_input")
    return result

if __name__ == "__main__":
    app.run(debug=True)
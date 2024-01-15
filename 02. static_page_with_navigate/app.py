# 2. Build a Flask app with static HTML pages and navigate between them.
from flask import Flask, render_template
app = Flask(__name__)
# on home page 
@app.route("/")
def home_page():
    return render_template("index.html")

# on about 
@app.route("/about")
def about_page():
    return render_template("about.html")

# run app 
if __name__ == "__main__":
    app.run(debug=True)
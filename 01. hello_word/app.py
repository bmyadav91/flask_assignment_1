# 1. Create a Flask app that displays "Hello, World!" on the homepage.
# import flask 
from flask import Flask
# assign to flask 
app = Flask(__name__)
# route on home page 
@app.route("/")
# creating hello_world function 
def hello_world():
    return "Hello World"

# run Environment 
if __name__ == "__main__":
    app.run(debug=True)

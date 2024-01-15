from flask import Flask, render_template, abort
app = Flask(__name__)

# 404 page not found error 
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

# server error 
@app.errorhandler(500)
def server_error(error):
    return render_template("500.html"), 500


# display internal server error 
@app.route('/error500')
def error_500():
    abort(500)


# home page 
@app.route("/")
def home_page():
    return render_template("index.html")


# run Environment 
if __name__ == "__main__":
    app.run(debug=True)

# 3. Develop a Flask app that uses URL parameters to display dynamic content.
from flask import Flask, request
app = Flask(__name__)
contentt = "Write There or here conent"
# pass this url if running in localhost "http://127.0.0.1:5000/?content=hello"
@app.route("/")
def url_para():
    data = request.args.get("content")
    return data
# run app
if __name__ == "__main__":
    app.run(debug=True)
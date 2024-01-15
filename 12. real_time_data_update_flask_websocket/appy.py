from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

# home page 
home_data = 11
@app.route("/")
def home_page():
    return render_template("index.html", home_data=home_data)

# update render 
@app.route("/update")
def update_page():
    return render_template("update.html")

@socketio.on("socket_update_val")
def update_value(data):
    global home_data
    home_data = data
    socketio.emit("socket_update_val", home_data, namespace='/')


# run Environment
if __name__ == "__main__":
    socketio.run(app, debug=True)
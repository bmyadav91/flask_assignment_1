from flask import Flask, render_template
from flask_socketio import SocketIO
app = Flask(__name__)
socket = SocketIO(app)

# home page 
@app.route("/")
def home_page():
    return render_template("index.html")

# notify user 
@app.route("/notify")
def notify_page():
    return render_template("notify.html")

# data store 
notification_data = ""
data_html = '''<div class="alert alert-warning alert-dismissible fade show" role="alert">
        <strong>Notification!</strong> {notification_data}
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
    </div>'''

# notify websocket 
@socket.on("notify")
def notify_data(data):
    global data_html, notification_data
    notification_data = data
    format_html_data = data_html.format(notification_data=notification_data)
    socket.emit("notify", format_html_data)



# run Environment
if __name__ == "__main__":
    socket.run(app, debug=True)
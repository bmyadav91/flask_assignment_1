from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print('Message:', msg)
    socketio.emit('message', msg, namespace='/')

if __name__ == '__main__':
    socketio.run(app, debug=True)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/callback', methods=['POST'])
def callback():
    print("Treinamento encerrado")
    return '', 204
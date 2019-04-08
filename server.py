from flask import Flask
app = Flask(__name__)

@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')
def hello_world(path):
    return 'Hello, World!'

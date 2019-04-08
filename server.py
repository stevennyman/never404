from flask import Flask
app = Flask(__name__)

@app.route('/', defaults={'dummy': ''})
@app.route('/<path:dummy>')
def hello_world(dummy):
    return 'Hello, World!'

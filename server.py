from flask import Flask
app = Flask(__name__)

@app.route('/', defaults={'dummy': ''}) # URL catching based on: http://flask.pocoo.org/snippets/57/ and https://stackoverflow.com/a/14023930
@app.route('/<path:dummy>')
def hello_world(dummy):
    return 'Hello, World!'

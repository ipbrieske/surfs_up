from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello world'

@app.route('/about')

def about():
    return 'The hokey pokey - that\'s what it\'s all about!'
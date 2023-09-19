#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views.</h1>'

@app.route('/print/<string:name>')
def print_string(name):
    print(name)

    return f'<h1>{name}<h1>'

@app.route('/count/<int:param>')
def count(param):
    numbers = '\n'.join(str(i) for i in range(1, param + 1))
    return f'<pre>{numbers}</pre>'    

if __name__ == '__main__':
    app.run(port=5555, debug=True)

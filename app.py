from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/json')
def hello_json():
    data = {
        'msg':'Hello, World!',
        'decimal':15
    }
    return jsonify(data)

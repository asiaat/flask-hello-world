from flask import Flask,jsonify,request
import urllib.request 
import json
import requests
#from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont
from certify import generate_certificate

proj_id = '2TEasvlIepRnGZwQWKGjy4PcRVS'
proj_secret = '3f71ebe5ea462f4bb1c78f70bbb812ee'


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

@app.route('/get_ipfs/<cid>')
def get_ipfs(cid):
    
    #arg = "QmPmHk4MpNifLFxBzoCtwdiAHJSy8QKhRvN5eiaCYJKdkV"
    arg =str(cid)
    url = f"https://ipfs.infura.io:5001/api/v0/get?arg={arg}&archive=true"
    
    response = requests.post(url, auth=(proj_id, proj_secret))

    return response.text


@app.route('/put_ipfs/')
def put_ipfs():

    url = "https://ipfs.infura.io:5001/api/v0/add?pin=false"    
    # Prepare the file payload
    file_path = "probe/sample-result.json"
    files = {'file': open(file_path, 'rb')}
    
    
    response = requests.post(url, 
                            auth=(proj_id, proj_secret),
                            files=files
                            )

    return response.text

@app.route('/post_json', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return json
    else:
        return 'Content-Type not supported!'
    
@app.route('/create_json/<cuteness>')
def create_json(cuteness):
    
    json_data = {
        "name": "PUG",
        "description": "An adorable PUG pup!",
        "image": "https://ipfs.io/ipfs/QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8?filename=pug.png",
        "attributes": [
            {
                "trait_type": "cuteness",
                
                
                "value": int(cuteness)
            },
            {
                "trait_type": "hairy",
                "value": 81
            }
        ]
    }
    
    name = "Halter"
    issued_date = "July 29, 2023"
    certificate_holder = "John Doe"
    quantum_computer = "QuantumLab-1"
    num_qubits = 50

    generate_certificate(name, issued_date, certificate_holder, quantum_computer, num_qubits)
    
    return json_data
    

        
        
        


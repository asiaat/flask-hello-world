from flask import Flask,jsonify,request
import urllib.request 
import json
import requests
#from dotenv import load_dotenv

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
    

        
        
        


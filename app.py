from flask import Flask,jsonify
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


        
        
        


from flask import Flask,jsonify,request
import requests
from certify import generate_certificate, create_erc721_metadata
from   datetime import datetime 
from lib.quantumcomp import backend_name

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

@app.route('/list')
def hello_list():
    data = [{
        'msg':'Hello, World!',
        'decimal':15
    }]
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

    
@app.route('/create_json/<cuteness>')
def create_json(cuteness):
    
    name = "Halter2"
    issued_date = "July 29, 2023"
    certificate_holder = "John Doe"
    quantum_computer = "QuantumLab-1"
    num_qubits = 30

    generate_certificate(name, issued_date, certificate_holder, quantum_computer, num_qubits)
    
    return name

@app.route('/put_cert/')
def put_cert():

    url = "https://ipfs.infura.io:5001/api/v0/add?pin=false"    
    # Prepare the file payload
    file_path = "certs/Quantum_Teleportation_Cert_Halter2.png"
    files = {'file': open(file_path, 'rb')}
    
    
    response = requests.post(url, 
                            auth=(proj_id, proj_secret),
                            files=files
                            )
    # Check the response
    json_out = {}
    if response.status_code == 200:
        ipfs_hash = response.json()['Hash']
        print("File uploaded to IPFS with hash:", ipfs_hash)
        json_out = {
            "msg":"File uploaded to IPFS with hash",
            "hash":ipfs_hash
        }
        
        url2 = "https://ipfs.infura.io:5001/api/v0/add?pin=false"    
        # Prepare the file payload
        
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        new_json_file = f"certs/metadata-{timestamp}.json"
        file_path2 = create_erc721_metadata(new_json_file,
                        22,
                        ipfs_hash,
                        33,
                        66
                        )
        
        files2 = {'file': open(file_path2, 'rb')}
  
        response2 = requests.post(url2, 
                                auth=(proj_id, proj_secret),
                                files=files2
                                )
        
        if response2.status_code == 200:
            ipfs_hash = response2.json()['Hash']
            print("JSON File uploaded to IPFS with hash:", ipfs_hash)
            json_out = {
                "msg":"File uploaded to IPFS with hash",
                "hash":ipfs_hash
            }
        else:
            print("Error:", response.text)
            json_out = {
                "msg":"Error",
                "error":response.text
            }
        
        
    else:
        print("Error:", response.text)
        json_out = {
            "msg":"Error",
            "error":response.text
        }

    return json_out
    


        
        


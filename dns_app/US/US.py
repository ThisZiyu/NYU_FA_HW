import logging
from socket import *
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/fibonacci', methods=['GET'])
def calculate_fibonacci():
    # Get parameters from the request
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')

    print(hostname,fs_port,number,as_ip,as_port)
    # Check if any parameter is missing
    if None in (hostname, fs_port, number, as_ip, as_port):
        return jsonify({'error': 'Bad request'}), 400

    # Create a UDP socket
    client = socket(AF_INET,SOCK_DGRAM)

    # Send a message to the AS server
    msg = "TYPE=A\nNAME={}".format(hostname)
    print(msg)
    client.sendto(msg.encode(), (as_ip, int(as_port)))

    # Receive a response from the AS server
    msg_back, _ = client.recvfrom(1024)
    client.close()

    logging.info(msg_back.decode())
    name,output = splitmsg(msg_back.decode())
    # Make a request to this service with the result from AS
    r = requests.get(f"http://{output}:{fs_port}/fibonacci?number={number}")
    return jsonify(r.json()), 200

def splitmsg(msg):
    msg = msg.split('\n')
    result = msg[1].split('=')[1]
    output = msg[2].split('=')[1]
    return result, output


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

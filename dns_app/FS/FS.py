from flask import Flask, request, jsonify
from socket import *
import json

app = Flask(__name__)


@app.route('/register', methods=['PUT'])
def register():
    try:
        data = request.get_json()
        hostname = data.get('hostname')
        ip = data.get('ip')
        as_ip = data.get('as_ip')
        as_port = data.get('as_port')
        #print(data)

        if None in (hostname, ip, as_ip, as_port):
            return jsonify({'error': 'Bad request'}), 400
        else:
            client = socket(AF_INET, SOCK_DGRAM)
            msg = "Type=A\nName={}\nVALUE={}\nTTL=10".format(hostname,ip)
            client.sendto(msg.encode(), (as_ip, int(as_port)))
            msg_back, IPaddress = client.recvfrom(1024)
            print(msg_back.decode())
            client.close()
            if msg_back.decode() == 'Success':
                return jsonify({'message': 'Registered successfully'}), 201
        return jsonify({'error': 'Registration failed'}), 500

    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid JSON format'}), 400

@app.route('/fibonacci', methods=['GET'])
def calculate_fibonacci():
    number = request.args.get('number')

    try:
        n = int(number)
        if n < 0:
            return jsonify({'error': 'Negative sequence number not supported'}), 400

        # Calculate Fibonacci number for the sequence number
        result = calculate_fibonacci_value(n)
        return jsonify('The fibonacci value of {} is {}'.format(number,result)), 200
    except ValueError:
        return jsonify({'error': 'Bad request, number must be an integer'}), 400

# Function to calculate Fibonacci number
def calculate_fibonacci_value(n):
    if n < 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n==2:
        return 1
    else:
        return calculate_fibonacci_value(n-1)+calculate_fibonacci_value(n-2)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9090,debug=True)

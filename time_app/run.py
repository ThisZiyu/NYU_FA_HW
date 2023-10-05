from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world!'

@app.route('/time')
def return_time():
    current_time = datetime.now()
    time_str = current_time.strftime('%Y-%m-%d %H:%M:%S') 
    return jsonify({'The current time is': time_str})  

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=8080,
            debug=True)

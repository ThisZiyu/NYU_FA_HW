from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world!'

@app.route('/time')
def return_time():
    current_time = datetime.now()
    time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')  # 格式化时间为字符串
    return jsonify({'The current time is': time_str})  # 将时间字符串转换为 JSON 格式并返回

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=8080,
            debug=True)

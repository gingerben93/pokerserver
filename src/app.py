from flask import Flask, jsonify, request
import logging

log = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index_get():
    if(request.method == 'GET'):
        return jsonify({'Start': 'Hello World'})

@app.route("/", methods=['POST'])
def index_post():
    if(request.method == 'POST'):
        client_message = request.get_json()
        return jsonify({'post message': client_message})

@app.route("/", methods=['PUT'])
def index_put():
    if(request.method == 'PUT'):
        client_message = request.get_json()
        return jsonify({'put message': client_message})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

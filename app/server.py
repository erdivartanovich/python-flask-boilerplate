from flask import Flask, jsonify, json, request
from app import data

app = Flask(__name__)

@app.route('/list')
def list():
    print(request.args.get('user'))
    return jsonify(data)

@app.route('/add', methods=['POST'])
def addNewData():
    # menambahkan data todo
    newTodo = request.json
    data.append(newTodo)
    return jsonify(data)



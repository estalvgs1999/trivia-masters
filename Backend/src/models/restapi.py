# -----------------------------
# File: game.py
# Project: Trivia
# dev by: @estalvgs1999
#
# Description: Restful API service
# to control client interaction w/
# game logic.
#
# version 0.1
# last edited: 7/4/20 [20:40]
#
# an av_software project
#-------------------------------

from flask import Flask, jsonify, request
from json import dumps

app = Flask(__name__)

path = '/api/v1.0'

@app.route(path+'/category', methods=['GET'])
def get_random_category():
    return jsonify({'msg':'hello'}) 

@app.route(path+'/question', methods=['GET'])
def get_random_question():
    print(request.json)
    return jsonify({'question':'¿1+1?'})

@app.route(path+'/answer', methods=['POST'])
def verify_answer():
    return {'answer':true}

if __name__ == "__main__":
    app.run(port=8080)
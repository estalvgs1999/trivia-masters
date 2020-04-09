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
# last edited: 7/4/20 [23:00]
#
# an av_software project
#-------------------------------

from flask import Flask, jsonify, request
from json import dumps
from game import game

app = Flask(__name__)

path = '/api/v1.0'

@app.route(path+'/category', methods=['GET'])
def get_random_category():
    game.select_category()
    return jsonify({'msg':'hello'}) 

@app.route(path+'/question', methods=['GET'])
def get_random_question():
    print(request.json)
    r = game.select_question(request.json['category'],request.json['level'])
    return jsonify(r)

@app.route(path+'/answer', methods=['POST'])
def verify_answer():
    game.validate_answer(request.json['q_id'],request.json['answer'])
    # TODO: Enviar toda la información de este turno
    return jsonify({'answer':true})

def run_api():
    app.run(port=8080)

if __name__ == "__main__":
    run_api()
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
from game import game

app = Flask(__name__)

path = '/api/v1.0'

@app.route(path+'/points', methods=['GET'])
def get_points():
    return jsonify({'a_points':game.team_a_points,'b_points':game.team_b_points})

@app.route(path+'/category', methods=['GET'])
def get_random_category():
    select_category = game.select_category()
    return jsonify({'category':select_category}) 

@app.route(path+'/question', methods=['POST'])
def get_random_question():
    print(request.json)
    selected_qustion = game.select_question(request.json['category'],request.json['level'])
    return jsonify({"question":selected_qustion,'a_points':game.team_a_points,'b_points':game.team_b_points})

@app.route(path+'/answer', methods=['POST'])
def verify_answer():
    print(request.json)
    answer_state = game.validate_answer(request.json['question'],request.json['answer'])
    return jsonify({'state':answer_state})

def run_api():
    app.run(port=8080)

if __name__ == "__main__":
    run_api()
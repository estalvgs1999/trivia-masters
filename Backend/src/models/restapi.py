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

from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

class Game_resources(Resource):

    def get(self):
       return {'msg':'hello'} 


api.add_resource(Game_resources,'/saludo') 

if __name__ == "__main__":
    app.run(port=8080)
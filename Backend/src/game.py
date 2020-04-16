# -----------------------------
# File: game.py
# Project: Trivia
# dev by: @estalvgs1999
#
# Description: Control everything 
# related to game logic.
#
# version 0.1
# last edited: 7/4/20 [23:00]
#
# an av_software project
#-------------------------------


from questions import *
import random
from json import dumps


class Game:

    def __init__(self):

        self.team_a_points = 0
        self.team_b_points = 0
        self.current_team = 0 # team A: 0 | team b: 1
        self.plays =  0
        
        # read from config file
        self.max_plays = 0
        self.max_points = 0
        pass

    def get_config(self):
        pass


    def select_category(self):
        # TODO: Selecciona una categoría del archivo 
        pass

    def select_question(self, category, level = 'easy'):
        # TODO: Selecciona una pregunta del archivo 
        return random.choice(q).to_JSON()
        
    def validate_answer(self,question_id, answer):
        # TODO: Verifica la respuesta para una pregunta
        pass

    def add_points(self, points):
        if self.current_team:
            self.team_b_points+= points
            return 
        self.team_a_points+= points
        
    def next_team(self):
        self.current_team = not self.current_team
        self.plays += 1

# For singleton :)
game = Game()    



if __name__ == "__main__":
    print(game.select_question('a'))

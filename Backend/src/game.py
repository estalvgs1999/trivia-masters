# -----------------------------
# File: game.py
# Project: Trivia
# dev by: @estalvgs1999
#
# Description: Control everything 
# related to game logic.
#
# version 0.1
# last edited: 17/4/20 [23:00]
#
# an av_software project
#-------------------------------


import questions as qs
import os
import json
import random

file_dir = os.path.dirname(os.path.abspath(__file__))
directory_file = os.path.dirname(file_dir)
config_path =  directory_file + '/docs/config.json'


class Game:

    points = {'facil':1, 'dificil':3}
    def __init__(self):

        self.team_a_points = 0
        self.team_b_points = 0
        self.current_team = 0 # team A: 0 | team b: 1
        self.plays =  0
        
        # read from config file
        self.max_plays = 0
        self.max_points = 0
        self.question_set = qs.QuestionSet()
        
        self.set_config()


    # @brief - Extract configuration settings for the game
    def set_config(self):
        
        with open(config_path, 'r') as json_file:
                
                config_json = json.load(json_file)
                
                self.max_plays = config_json["max_plays"]
                self.max_points = config_json["max_points"]
                q_file = config_json["q_file"]

                self.question_set.loadQuestionSet(q_file)

        print('''--- INICIAR JUEGO --- \n+ Set: {0}\n+ Puntos Máximos: {1}\n+ Turnos Máximos: {2}'''.format(q_file, self.max_points, self.max_plays))
                

    def select_category(self):
       return self.question_set.getRandomCategory()

    def select_question(self, category, level = 'easy'):
        qs = self.question_set.getRandomQuestion(category,level)
        print(qs)
        return qs
        
    def validate_answer(self,question, answer):
        state = False
        if question['respuesta'] == answer:
            state = True
            self.add_points(question['points'])
        self.next_team()
        self.info()
        return state

    def add_points(self, points):
        if self.current_team:
            self.team_b_points+= points
            return 
        self.team_a_points+= points
        
    def next_team(self):
        self.current_team = not self.current_team
        self.plays += 1

    def info(self):
        '''
            Muestra en la consola los puntajes del juego.
        '''
        info = '''
        ------------ TRIVIA ----------
        
        Equipo 1: {0}    Equipo 2:{1}

        Turno: {2}
        ------------------------------
        '''.format(self.team_a_points,self.team_b_points, 'Equipo 1' if not self.current_team else 'Equipo 2')
        print(info)

# For singleton :)
game = Game()    



if __name__ == "__main__":
    game.info()

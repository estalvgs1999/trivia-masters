# -----------------------------
# File: game.py
# Project: Trivia
# dev by: @estalvgs1999
#
# Description: Control everything 
# related to game logic.
#
# version 0.1
# last edited: 7/4/20 [18:40]
#
# an av_software project
#-------------------------------

class Game:

    def __init__(self):
        self.team_a_points = 0
        self.team_b_points = 0
        self.current_team = 0 # team A: 0 | team b: 1
        self.plays =  0
        pass

    def select_category(self):
        # TODO: Selecciona una categoría del archivo 
        pass

    def select_question(self, category, level = 'easy'):
        # TODO: Selecciona una pregunta del archivo 
        pass

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

    def 

    


# For singleton :)
game = Game()    



if __name__ == "__main__":
    pass

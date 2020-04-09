# -----------------------------
# File: question.py
# Project: Trivia
# dev by: @estalvgs1999
#
# Description: Contains questions 
# and questions sets.
#
# version 0.1
# last edited: 7/4/20 [23:00]
#
# an av_software project
#-------------------------------

class Question:

    def __init__(self):

        self.q_id = -1

        self.category = 'default'
        self.level = 'easy'
        self.points = 1
        
        self.question = '¿?'
        self.options = {}
        self.answer = 'a'

    # @brief : Serializes the object in a dictionary with the 
    # necessary information for the client.
    def to_JSON(self):
        return {
            "q_id" : self.q_id,
            "category" : self.category,
            "question" : self.question,
            "options" : self.options
        }


class QuestionSet:

    def __init__(self):
        self.category = 'default'
        self.questions = []
    
    


def add_question_set():
    pass
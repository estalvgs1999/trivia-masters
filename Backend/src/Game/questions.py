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

class QuestionSet:

    def __init__(self):
        self.__categories = {}
        print('ok')

    def loadQuestionSet(self, filePath):
        
    
    def __setCategories(self, questionSet):
        self.__categories = list(questionSet.keys())
        print('>> Categorías del juego: {}'.format(self.__categories))

    def getCategories(self):
        return self.__categories
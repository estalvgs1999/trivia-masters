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
import os
import json
import random

file_dir = os.path.dirname(os.path.abspath(__file__))
directory_file = os.path.dirname(file_dir)
config_path =  directory_file + '/docs/'

class QuestionSet:

    def __init__(self):
        self.__categories = []
        self.__questions = {}
        print('--- Question Set ---')


    def loadQuestionSet(self, filename):
        self.__questions = self.__getJson(filename)
        self.__setCategories()
    
    def __setCategories(self):
        self.__categories = list(self.__questions.keys())
        print('>> Categorías del juego: {}'.format(self.__categories))


    # @brief - It is responsible for reading the configuration
    #          json and returns it as a dictionary
    def __getJson(self,filename):
        with open(config_path+filename, 'r') as json_file:
            ds_json = json.load(json_file)
            return ds_json


    def getCategories(self):
        return self.__categories


    def getQuestions(self):
        return self.__questions


    def gerRandomCategory(self):
        return random.choice(self.__categories)

    def getRandomQuestion(self, category,level):
        return random.choice(self.__questions[category][level])



if __name__ == "__main__":
    pg = QuestionSet()
    pg.loadQuestionSet('lucas.json')
    
    ct = pg.gerRandomCategory()
    print(ct)

    print(pg.getRandomQuestion(ct,'facil'))


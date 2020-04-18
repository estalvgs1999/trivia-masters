# -----------------------------
# File: question.py
# Project: Trivia
# dev by: @estalvgs1999
#
# Description: Contains questions 
# and questions sets.
#
# version 0.1
# last edited: 17/4/20 [23:00]
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
        try:
            with open(config_path+filename, 'r') as json_file:
                ds_json = json.load(json_file)
                return ds_json
        except:
            print("Error 404 File not found")
            return -1

    def getCategories(self):
        return self.__categories

    def getQuestions(self):
        return self.__questions

    def getRandomCategory(self):
        return random.choice(self.__categories)

    def getRandomQuestion(self, category,level):
        try:
            qs = random.choice(self.__questions[category][level])
            self.__questions[category][level].remove(qs)
            return qs
        except IndexError:
            return {
                "enunciado": "Ya no hay más preguntas en la categoría {0}, nivel {1}".format(category,level),
                "opciones": {
                    "a": "",
                    "b": "",
                    "c": "",
                    "d": "Continuar"
                },
                "respuesta": "d",
                "points": 0
            }


if __name__ == "__main__":
    pg = QuestionSet()
    pg.loadQuestionSet('set_varios1.json')
    
    ct = pg.getRandomCategory()
    print(ct)

    print(pg.getRandomQuestion(ct,'facil'))


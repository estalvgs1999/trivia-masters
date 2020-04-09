# ------------------------------------------------------------
# File: json_utils.py
# Project: Trivia
# dev by: @estalvgs1999
#
# Description: This code is responsible for reading and
#              modifying the json file of game settings.
#
# version: 1.0
# last edited: 7/4/2020 [19:00]
#
# an av software project
# ------------------------------------------------------------

import os
import json

file_dir = os.path.dirname(os.path.abspath(__file__))
directory_file = os.path.dirname(os.path.dirname(file_dir))
config_path =  directory_file + '/data/'

# @brief - It is responsible for reading the configuration
#          json and returns it as a dictionary.
def get_json(file_name):
    with open(config_path+file_name, 'r') as json_file:
        config_json = json.load(json_file)
    return config_json

# @brief - Write the new dictionary with the new configuration in the json
# @param new_json_dict
def save_json(new_json):
    with open(config_path, 'w') as json_file:
        json.dump(new_json, json_file,indent=4)


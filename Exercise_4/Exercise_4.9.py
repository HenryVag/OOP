#File name: Exercise_4.9.py
#Author: Henry Våg
#Description: Exercise 4.9

import json
#make open file method instead of repeating opening the file
#format the output



with open("part.json") as file:
    data = file.read()

players = json.loads(data)

"""
for player in players:
    print(player["name"])
"""

class StatisticsBook:

    def __init__(self):
        self.file = None
    

    def set_file(self, filename):
        self.file = filename
        print(f"file is set to {filename}")

    def search_stats_by_name(self, name):
        with open(self.file) as file:
            data = file.read()
        players = json.loads(data)
        for player in players:
            if player["name"] == name:
                formatted_plus = f"{"+" :>30}"
                return f"{player["name"]}  {player["team"]:>22}  {player["goals"]} {formatted_plus} {player["assists"]} = {player["goals"] + player["assists"]}"
        
        return "player not found"
    

    def list_all_team_abbreviatons(self):
        abbreviations = []
        with open(self.file) as file:
            data = file.read()
        players = json.loads(data)
        for player in players:
            if player["team"] not in abbreviations:
                abbreviations.append(player["team"])
        abbreviations.sort()
        return abbreviations


    def list_all_countries(self):
        countries = []
        with open(self.file) as file:
            data = file.read()
        players = json.loads(data)
        for player in players:
            if player["nationality"] not in countries:
                countries.append(player["nationality"])
        countries.sort()
        return countries








stats = StatisticsBook()

stats.set_file("part.json")
print(stats.search_stats_by_name("Travis Zajac"))
print(stats.list_all_team_abbreviatons())
print(stats.list_all_countries())
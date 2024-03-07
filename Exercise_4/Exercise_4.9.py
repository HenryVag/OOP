#File name: Exercise_4.9.py
#Author: Henry Våg
#Description: Exercise 4.9

import json, os



class StatisticsBook:

    def __init__(self):
        self.file = None
    

    def set_file(self, filename):
        BASE_PATH = "C:/Users/Henry/Documents/Koulu\Amk/OOP24/" 
        full_path = os.path.join(BASE_PATH, filename)
        if os.path.exists(full_path):
            self.file = filename
            print(f"file is set to {filename}")
            return True
        else:
            print("file not found, please try again")
            return False

    def search_stats_by_name(self, name):
        players = self.open_json()
        for player in players:
            if name == player["name"]:
                player = [player for player in players if player["name"] == name]
        
                formatted_player = [
                    f"{player['name']:20} {player['team']:5}"
                    f"{player['goals']:>2} + {player['assists']:1} = {player['goals'] + player['assists']}"
                    for player in player
                ]
                return  "\n".join(formatted_player)
        
        return "player not found"
    

    def list_all_team_abbreviatons(self):
        abbreviations = []
        players = self.open_json()
        for player in players:
            if player["team"] not in abbreviations:
                abbreviations.append(player["team"])
        abbreviations.sort()
        return "\n".join(abbreviations)


    def list_all_countries(self):
        countries = []
        players = self.open_json()
        for player in players:
            if player["nationality"] not in countries:
                countries.append(player["nationality"])
        countries.sort()
        return "\n".join(countries)

    def list_players_in_team(self, team):
        team_players = []
        players = self.open_json()
        team_players = [player for player in players if player["team"] == team]
        team_players.sort(key=lambda player: player["goals"] + player["assists"], reverse=True)
        
        formatted_players = [
            f"{player['name']:20} {player['team']:5}"
            f"{player['goals']:>2} + {player['assists']:1} = {player['goals'] + player['assists']}"
            for player in team_players
        ]

        return "\n".join(formatted_players)
    
    def list_players_from_country(self, country):
        
        players = self.open_json()
        #Adds player to list for player in players if their nationality == country
        country_players = [player for player in players if player["nationality"] == country]

        # Sort players based on points (goals + assists) in descending order, lambda function = anonymous function, takes player as argument and returns total points
        country_players.sort(key=lambda player: player["goals"] + player["assists"], reverse=True)
        
        # Create a formatted result for each player
        formatted_players = [
            f"{player['name']:20} {player['team']:5}"
            f"{player['goals']:>2} + {player['assists']:1} = {player['goals'] + player['assists']}"
            for player in country_players
        ]
        
        #joins all the elements in the formatted players list into a single string, separated by a new line
        return "\n".join(formatted_players)
       

    def list_most_points(self, amount):
        players = self.open_json()
        all_players = [player for player in players]
        
        all_players.sort(key=lambda player: (player["goals"] + player["assists"], player["goals"]), reverse=True)
        top_players = all_players[:amount]
        
        formatted_players = [
            f"{player['name']:20} {player['team']:5}"
            f"{player['goals']:>2} + {player['assists']:1} = {player['goals'] + player['assists']}"
            for player in top_players
                
        ]

        return "\n".join(formatted_players)

    def list_most_goals(self, amount):
        players = self.open_json()
        all_players = [player for player in players]
        
        #the more games, the smaller the number -> the less games, the bigger the number
        all_players.sort(key=lambda player: (player["goals"], -player["games"]), reverse=True)
        top_scorers = all_players[:amount]
        
        formatted_players = [
            f"{player['name']:20} {player['team']:5}"
            f"{player['goals']:>2} + {player['assists']:1} = {player['goals'] + player['assists']}"
            for player in top_scorers
                
        ]

        return "\n".join(formatted_players)
    
    def open_json(self):
        with open(self.file) as file:
            data = file.read()

        return json.loads(data)



class StatsBookApp:

    def __init__(self):
        self._stats = StatisticsBook()

    def run(self):
        accessed_file = self.select_json()
       
        if accessed_file:
            while True:
                print("")
                print(f"read the data of {len(self._stats.open_json())} players")
                self.commands()
                command = input("command:")

                if command == "0":
                    print("quitting")
                    break 
                if command == "1":
                    name = input("name:")
                    print(self._stats.search_stats_by_name(name))
                if command == "2":
                    print(self._stats.list_all_team_abbreviatons())
                if command == "3":
                    print(self._stats.list_all_countries())
                if command == "4":
                    team = input("team:")
                    print(self._stats.list_players_in_team(team))
                if command == "5":
                    country = input("country:")
                    print(self._stats.list_players_from_country(country))
                if command == "6":
                    player_count = input("how many:")
                    print(self._stats.list_most_points(int(player_count)))
                if command == "7":
                    player_count = input("how many:")
                    print(self._stats.list_most_goals(int(player_count)))

        else:
            self.run()

    def select_json(self):
        name = input("file name:")
        file_name = self._stats.set_file(name)
        return file_name


    def commands(self):
        print("commands:")
        print("---------------------------")
        print("0 exit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals\n")







def main():
    
    stats = StatsBookApp()
    stats.run()


if __name__ == "__main__":
    main()

#Author: Henry Våg
#File name: Exercise_3.9.py
#Description: Exercise 3.9

class WeatherStation:

    observations = []

    def __init__(self, name):
        self.name = name
        

    def __str__(self):
        return f'Name: {self.name}, {len(WeatherStation.observations)} observations'

    @staticmethod
    def add_observation(observation: str):
        
        WeatherStation.observations.append(observation)
        latest_observation = len(WeatherStation.observations)-1
        print("Observation added:", WeatherStation.observations[latest_observation])

    @staticmethod
    def latest_observation():
        if not WeatherStation.observations == False:
            latest_observation = len(WeatherStation.observations)-1
            return WeatherStation.observations[latest_observation]
        else:
            return ""
    #Total number of observations from all stations    
    @staticmethod
    def number_of_observations():
        return len(WeatherStation.observations)

station =WeatherStation("Houston")
station.add_observation("Rain 10mm")
station.add_observation("Sunny")
print(station.latest_observation())
station.add_observation("Thunderstorm")
print(station.latest_observation())
print(station.number_of_observations())
print(station)



#Author: Henry Våg
#File name: Exercise_3.9.py
#Description: Exercise 3.9

class WeatherStation:

    __observations = []

    def __init__(self, name):
        self.__name = name
        

    def __str__(self):
        return f'Name: {self.__name}, {len(WeatherStation.__observations)} observations'

    @staticmethod
    def add_observation(observation: str):
        
        WeatherStation.__observations.append(observation)
        latest_observation = len(WeatherStation.__observations)-1
        print("Observation added:", WeatherStation.__observations[latest_observation])

    @staticmethod
    def latest_observation():
        if  WeatherStation.__observations == True:
            latest_observation = len(WeatherStation.__observations)-1
            return WeatherStation.__observations[latest_observation]
        else:
            return ""
    #Total number of observations from all stations    
    @staticmethod
    def number_of_observations():
        return len(WeatherStation.__observations)

station =WeatherStation("Houston")
station.add_observation("Rain 10mm")
station.add_observation("Sunny")
print(station.latest_observation())
station.add_observation("Thunderstorm")
print(station.latest_observation())
print(station.number_of_observations())
print(station)



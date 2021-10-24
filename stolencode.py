import requests
import random
from matplotlib import pyplot as plt
from time import sleep

class Environment:
    """Getting 5 day weather forecast from weather API and choosing soil type that would be 
    the base information for the plant growth"""
    def __init__(self, weather = None, temperature = None, temp_return = None, soil_type = None):
        self.weather = weather
        self.temperature = temperature
        self.temp_return = temp_return
        self.soil_type = soil_type
        self.daily_weather_list = []

    def get_weather(self):
        # Error checking format
        while True:
            self.zip_code = input("Enter your zip code to get weather info: ")
            print('-'*30,"\n")
            self.url = "http://api.openweathermap.org/data/2.5/forecast?appid=a9fed4c32128f18e6142d3bd49fb5f7d&units=metric&zip=" + self.zip_code
            self.response = requests.get(self.url) 
            self.result = self.response.json()
            if self.result["cod"] != "404":
                self.weather_list = self.result['list']
                a = -8 
                # Extract 5 day weather forecast from json format
                for i in range(1, int(round((len(self.weather_list))/8+1,0))):
                    a += 8
                    self.weather = self.result['list'][a]['weather'][0]['description']
                    self.temperature = self.result['list'][a]['main']['temp']
                    self.daily_weather_list.append(self.weather)

                    print("Day", i, "Weather: {}".format(self.result['list'][a]['weather'][0]['description']))
                    print("Day", i, "Temperature: {} °C".format(self.result['list'][a]['main']['temp']))
                    print('-'*30, "\n")

                    if self.temperature >= 35:
                        self.temp_return = "high"
                    elif 35 > self.temperature >= 10:
                        self.temp_return = "moderate"
                    else:
                        self.temp_return = "low"
                break

            else:
                print("***ZIP CODE NOT FOUND***\n")

    def choose_soil_type(self):
        # Error checking format
        while True:
            self.soil_type = input("Please choose soil type - [1]-alkaline, [2]-neutral, [3]-acidic: ")
            print('-'*30, "\n")
            if self.soil_type not in '123':
                print("***NOT A VALID SOIL TYPE***")
            else:
                break

class Plants:
    """User choice of plants. After the selection, properties of the selected plant are provided."""
    def __init__(self, preferred_sunshine = None, preferred_water = None, preferred_fertilizer = None, preferred_temp = None, preferred_soil = None):
        self.preferred_sunshine = preferred_sunshine
        self.preferred_water = preferred_water
        self.preferred_fertilizer = preferred_fertilizer
        self.preferred_temp = preferred_temp
        self.preferred_soil = preferred_soil

    def choose_plant(self):
        while True:
            print("**Plant information")
            print("*lemon - prefer moderate water, less fertilizer, neutral soil")
            print("*blueberry - prefer more water, moderate fertilizer, acidic soil")
            print("*pear - prefer less water, more fertilizer, alkaline soil\n")
            sleep(1)
            self.choose = input("Please choose your plant to breed [1]-lemon, [2]-blueberry, [3]-pear): ")
            print('-'*30, "\n")

            # Error checking if wrong plant name is entered
            if self.choose not in '123':
                print("***NOT A VALID PLANT***\n")
                continue
            # Locate properties of each plant
            if self.choose == "1":
                self.preferred_sunshine = 9
                self.preferred_water = 5
                self.preferred_fertilizer = 3
                self.preferred_temp = "high"
                self.preferred_soil = "neutral"
                break
            elif self.choose == "2":
                self.preferred_sunshine = 6
                self.preferred_water = 8
                self.preferred_fertilizer = 5
                self.preferred_temp = "moderate"
                self.preferred_soil = "acidic"
                break
            elif self.choose == "3":
                self.preferred_sunshine = 3
                self.preferred_water = 3
                self.preferred_fertilizer = 7
                self.preferred_temp = "low"
                self.preferred_soil = "alkaline"
                break

        print("Next, you have to determine the amount of water and fertilizer in consideration of the weather.\n")
        sleep(2)
        print("Removing weed would be automatically performed, and you will get the full score if it is done in 3 times.\n")
        sleep(2)
        print("The goal is to reach 500% fruit growth for 5 days.")
        print('-'*30, "\n")

class Growth:
    """Based on the plant choice and environment settings, user can select treatment amounts for each day,
    and calculate accumulated fruit size to determine success or failure."""
    def __init__(self, Environment, Plants, water = 0, fertilizer = 0, weed = True):
        self.Environment = Environment
        self.Plants = Plants
        self.water = water
        self.fertilizer = fertilizer
        self.weed = weed

    def treatment(self):
        self.plot_list = []
        self.tracker = 1
        self.fruit_size = 0.1
        # 5 day iteration from each day's weather forecast
        for items in self.Environment.daily_weather_list:
            # Adjust preferred amount of water based on the weather forecast
            if "rain" in items.lower() and "drizzle" not in items.lower():
                self.Plants.preferred_water -= 3
                print("Since it's raining, try to decrease the amount of water.\n")
                sleep(1)
            elif "drizzle" in items.lower():
                self.Plants.preferred_water -= 1
                print("Since it's drizzling, try to decrease the amount of water a little bit.\n")
                sleep(1)
            elif "clear sky" in items.lower():
                self.Plants.preferred_water += 2
                print("Since it's sunny outside, try to increase the amount of water.\n")
                sleep(1)

            # Error checking format
            # Determine effectiveness of water and fertilizer amount
            while True:
                print("Day", self.tracker)
                self.water = int(input("Please enter the amount of water (scale 0-10): "))
                if self.water not in range(11):
                    print("***NOT A VALID AMOUNT***")
                    continue
                if self.water == self.Plants.preferred_water:
                    self.water_score = 10
                    break
                elif self.Plants.preferred_water - 2 <= self.water <= self.Plants.preferred_water + 2:
                    self.water_score = 7
                    break
                else:
                    self.water_score = 4 
                    break

            while True:
                self.fertilizer = int(input("Please enter the amount of fertilizer (scale 0-10): "))
                if self.fertilizer not in range(11):
                    print("***NOT A VALID AMOUNT***")
                    continue
                if self.fertilizer == self.Plants.preferred_fertilizer:
                    self.fertilizer_score = 10
                    break
                elif self.Plants.preferred_fertilizer - 2 <= self.fertilizer <= self.Plants.preferred_fertilizer + 2:
                    self.fertilizer_score = 7
                    break
                else:
                    self.fertilizer_score = 4  
                    break

            # Automated weed removal: random score
            count = 0
            while self.weed == True:
                x = 1* random.random()
                count += 1
                if x < 0.3:
                    print("You have removed the weeds", count, "times to help the plant grow. Good job!\n")
                    break
            if count <= 3:
                self.weed_score = 10
            else:
                self.weed_score = 5

            # Calculate probability of fruit growth. Weight of parameters: water 30%, fertilizer 30%, soil type 10%, - user selection
            # weed 20%, temperature 10% - random
            self.probability = 0
            if self.Environment.soil_type == self.Plants.preferred_soil:
                self.probability += random.uniform(0.7, 0.9) * 0.1
            else:
                self.probability += random.uniform(0.3, 0.5) * 0.1

            if self.Environment.temp_return == self.Plants.preferred_temp:
                self.probability += random.uniform(0.7, 0.9) * 0.1
            else:
                self.probability += random.uniform(0.3, 0.5) * 0.1

            if self.water_score == 10:
                self.probability += random.uniform(0.7, 0.9) * 0.3
            elif self.water_score == 7:
                self.probability += random.uniform(0.4, 0.6) * 0.3
            elif self.water_score == 4:
                self.probability += random.uniform(0.1, 0.3) * 0.3

            if self.fertilizer_score == 10:
                self.probability += random.uniform(0.7, 0.9) * 0.3
            elif self.fertilizer_score == 7:
                self.probability += random.uniform(0.4, 0.6) * 0.3
            elif self.fertilizer_score == 4:
                self.probability += random.uniform(0.1, 0.3) * 0.3

            if self.weed_score == 10:
                self.probability += random.uniform(0.7, 0.9) * 0.2
            else:
                self.probability += random.uniform(0.3, 0.5) * 0.2

            self.fruit_size = self.fruit_size + self.fruit_size * self.probability
            self.tracker += 1
            # For plotting fruit growth
            self.plot_list.append((self.tracker-1, round(((self.fruit_size - 0.1)/0.1)*100, 0)))
            print("Accumulated growth check: ", round(((self.fruit_size - 0.1)/0.1)*100, 0),"% growth")
            print('-'*30, "\n")

        print("Fruit size was increased by {}%".format(round(((self.fruit_size - 0.1)/0.1)*100, 0)))
        print('-'*30, "\n")

        # Determine the success or failure of fruit growth to a desired point
        if self.fruit_size > 0.6:
            print("Great job! You successfully raised the fruit of", self.Plants.choose, "to a desired point.")
        else:
            print("I'm sorry to inform you that you failed to raise the fruit of", self.Plants.choose, "to a desired point.")

class Growth_plot:
    """Plot of fruit growth progress"""
    def __init__(self, Growth):
        self.Growth = Growth

    def generate_plot(self):
        plt.scatter(*zip(*self.Growth.plot_list))
        plt.title('Fruit Growth Chart')
        plt.xlabel('Day')
        plt.ylabel('Growth %')
        plt.show()

def start_engine():
    """Core of the plant growth program."""
    print("Welcome to the plant growth game! Please select your location to grow your own plant of your choice.\n")
    sleep(1)
    a = Environment()
    a.get_weather()
    a.choose_soil_type()
    b = Plants()
    b.choose_plant()
    c = Growth(a, b)
    c.treatment()
    d = Growth_plot(c)
    d.generate_plot()

start_engine()
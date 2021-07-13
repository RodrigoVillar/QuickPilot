import json, requests, config
class Weather:

    city = ""

    weather_json = None

    def __init__(self):
        self.set_city()
    

    def run(self):
        while True:
            self.weather_instructions()
            while True:

                y = self.weather_json["main"]

                x = input("Input command here: ")

                if x == "temp":
                    result = y["temp"]
                    conversion = self.kelv_to_fahr(result)
                    print("The current temperature in your area is " + str(round(conversion, 2)) + " degrees fahreinheit!")
                    self.continue_instructions()
                elif x == 'all':
                    result_temp = y["temp"]
                    conversion_temp = self.kelv_to_fahr(result_temp)
                    result_feels = y['feels_like']
                    conversion_feels = self.kelv_to_fahr(result_feels)
                    print("The current temperature in your area is " + str(round(conversion_temp, 2)) + \
                        " degrees fahreinheit, although it feels like it is " + str(round(conversion_feels, 2)) + " degrees outside.")
                    print("The current humidity is " + str(y['humidity']) + "%.")
                    self.continue_instructions()
                elif x == 'humidity':
                    print("The current humidity is " + str(y['humidity']) + "%.")
                    self.continue_instructions()
                elif x == 'back':
                    return
                else:
                    print("Please enter a valid command!")
                    

    def weather_instructions(self):
        print("Welcome to the Weather Section of QuickPilot!")
        print("The following commands are available for the weather: 'all' - returns all available weather data, 'temp' - returns the temperature, 'humidity' - returns the humidity.")
        print("Additionally, you can enter 'back' return to the main menu")
    
    
    def continue_instructions(self):
        print("You can continue with any weather command or you can enter 'back' to return to the main menu!")


    def set_city(self):
        temp = input("Please type in a city name or valid zip code: ")
        self.get_weather_json(temp) # This gets the weather JSON we need


    def get_weather_json(self, city_name):

        api_key = config.weather_api_key
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        self.weather_json = response.json()
    
    
    def kelv_to_fahr(self, value):
        temp = 9 * (value - 273)
        result = (temp / 5) + 32
        return result

class Airport:

    airport_name = ""
    
    airport_json = None

    chosen_airport_json = None

    def __init__(self):
        self.airport_json_helper()
        self.set_airport_name()

    def run(self):
        while True:
            self.airport_instructions()
            while True:

                x = input("Input command here: ")

                if x == 'all':
                    self.airport_basic_action()
                    self.continue_instructions()
                elif x == 'back':
                    return
                elif x == 'elevation':
                    print("Your airport has an elevation of " + self.chosen_airport_json['elevation'] + " feet!")
                    self.continue_instructions()
                elif x == 'coordinates':
                    print("Your airport has the coordinates of " + self.chosen_airport_json['lat'] + ", " + self.chosen_airport_json['long'] + " (lon/lat)")
                    self.continue_instructions()
                elif x == 'show-commands':
                    self.show_commands()
                else:
                    print("Please enter a valid command!")


    def airport_instructions(self):
        print("\nWelcome to the Airport section of QuickPilot!\n")
        self.show_commands()

    def continue_instructions(self):
        print("You can continue with any airport command or you can enter 'back' to return to the main menu!")

    def show_commands(self):
        print("The following commands are available for your airport: 'all' - returns all available airport data, \
'elevation' - returns the elevation of your airport, 'coordinates' - returns the coordinates (lon/lat) of your airport, \
'back' - returns you to the main menu, 'show-commands' - displays all available commands")

    def set_airport_name(self):
        while True:
            temp = input("Please type in the ICAO code of an airport: ")
            if temp not in self.airport_json:
                print("Please input a valid ICAO airport code! ")
                continue
            else:
                self.airport_name = temp
                self.chosen_airport_json = self.airport_json[self.airport_name]
                break


    def airport_action(self):
        print("The following commands are available: 'basic' or 'advanced'.")
        while True: 
            temp = input("Please type in a valid command: ")
            if temp == 'basic':
                self.airport_basic_action()
                break
            elif temp == 'advanced':
                self.airport_advanced_action()
                break
            else:
                print("The command your entered is not valid!")
                continue


    def airport_json_helper(self):
        file = open('data/airports.json')
        fileData = file.read()
        self.airport_json = json.loads(fileData)
        file.close
        

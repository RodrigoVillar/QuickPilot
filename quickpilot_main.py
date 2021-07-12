import json, requests

class QuickPilot:

    allowed_commands = ('weather', 'airport')

    command = ""

    weather_obj = None

    airport_obj = None

    def __init__(self):
        self.user_instructions()

    def user_instructions(self):
        """
        Prints out actions user can take once the program has been initialized
        """
        print("Welcome to QuickPilot!\n\n\
From Here, you can take the following actions: \n\n \
    'weather' : find out the weather in your area\n \
    'airport' : get information about a specific airport.\n\n\
Additionally, you can use Control+C to exit out of this program at any time.")
    # LATER: use library to make this text look cleaner/more professional

    def set_command(self):
        while True:
            var = input()
            if var not in self.allowed_commands:
                print("Please input a valid command: ")
                continue
            else:
                self.command = var
                break
    

    def run_command(self):
        if self.command == "weather":
            self.weather_obj = Weather()
            self.weather_obj.set_city()
            self.weather_obj.actions()

        elif self.command == "airport":
            self.airport_obj = Airport()

class Weather:

    city = ""

    weather_json = None

    def __init__(self):
        print("initialized a weather object")

    def set_city(self):
        temp = input("Please type in a city name: ")
        self.get_weather_json(temp) # This gets the weather JSON we need

    def get_weather_json(self, city_name):

        api_key = "***REMOVED***"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        self.weather_json = response.json()

    def actions(self):
        print("Enter the command 'temp' to see the current temperature for your area")
        x = input("Input command here: ")

        if x == "temp":
            y = self.weather_json["main"]
            result = y["temp"]
            conversion = self.kelv_to_fahr(result)
            print("The current temperature in your area is " + str(round(conversion, 2)) + " degrees fahreinheit!")
    
    def kelv_to_fahr(self, value):
        temp = 9 * (value - 273)
        result = (temp / 5) + 32
        return result

class Airport:

    airport_name = ""
    
    airport_json = None

    def __init__(self):
        self.airport_json_helper()
        self.set_airport_name()
        self.airport_action()


    def set_airport_name(self):
        while True:
            temp = input("Please type in the ICAO code of an airport: ")
            if temp not in self.airport_json:
                print("Please input a valid ICAO airport code: ")
                continue
            else:
                self.airport_name = temp
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

    def airport_basic_action(self):
        toma = self.airport_json[self.airport_name]
        print("Your airport name is " + toma['name'] + ", which is located in " + toma["city"] + ", " + toma['state'] + ", " + toma["country"] + ".")

    def airport_advanced_action(self):
        print("advanced command!")
        

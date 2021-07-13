import quickpilot_main as qproutes

class QuickPilot:

    allowed_commands = ('weather', 'airport', 'back')

    command = ""

    weather_obj = None

    airport_obj = None

    def run(self):
        while True: # Makes it so that program doesn't end when the final command is inputted
            self.user_instructions()
            while True:
                var = input()
                if var not in self.allowed_commands:
                    print("Please input a valid command: ")
                    continue
                else:
                    if var == 'back':
                        quit()
                    self.command = var
                    if self.command == "weather":
                        self.weather_obj = qproutes.Weather()
                        self.weather_obj.run()
                    elif self.command == "airport":
                        self.airport_obj = qproutes.Airport()
                        self.airport_obj.run()
                    break


    def user_instructions(self):
        """
        Prints out actions user can take once the program has been initialized
        """
        print("Welcome to QuickPilot!\n\n\
From Here, you can take the following actions: \n\n \
    'weather' : find out the weather in your area\n \
    'airport' : get information about a specific airport.\n\n\
Additionally, you can use Control+C or 'back' to exit out of this program at any time.")
    # LATER: use library to make this text look cleaner/more professional
    #Test part 2
    
if __name__ == "__main__":
    x = QuickPilot()
    x.run()
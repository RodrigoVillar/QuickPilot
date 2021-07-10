class QuickPilot:

    allowed_commands = ('weather', 'airport')

    command = ""

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
        
        print("self.command is equal to: " + self.command)

    def run_command(self):
        if self.command == "weather":
            print("weather it is!")
        elif self.command == "airport":
            print("airport it is")

        
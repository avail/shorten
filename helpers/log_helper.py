


class Log():
    PINK 		= '\033[95m'
    BLUE 		= '\033[94m'
    GREEN 		= '\033[92m'
    YELLOW 		= '\033[93m'
    RED 		= '\033[91m'
    ENDC 		= '\033[0m'
    BOLD 		= '\033[1m'
    UNDERLINE 	= '\033[4m'


    def print(self, string, color):
        print("{}{}{}".format(color, string, self.ENDC))

    def printError(self, string):
        print("{}[ERROR]{} {}".format(self.RED, self.ENDC, string))


    def printSuccess(self, string):
        print("{}[SUCCESS]{} {}".format(self.GREEN, self.ENDC, string))
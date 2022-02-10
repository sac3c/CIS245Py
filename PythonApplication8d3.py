
class vehicle(object):
    "Parent class for vehicle features and options"
    def __init__ (self, make, model, color, fueltype, options):
        self.make = make          #input("Type in a car manufacturer ")
        self.model = model           #input("Type in a car model ")
        self.color =  color          #input("Type in a car color ")
        self.fueltype = fueltype        #input("Type in a car fuel type ")
        self.option =  options         #input("Type in a car option ")
        
    def getmake(self):
        return self.make

    def getmodel(self):
        return self.model

    def getcolor(self):
        return self.color

    def getfueltype(self):
        return self.fueltype

    def getoption(self):
        return self.options
    
    def display_info(self):
        #return '{} {} {} {} {}'.format(self.make, self.model, self.color, self.fueltype, self.option)
        print (f"You have a {self.make} {self.model} and it is {self.color} and has {self.option}")

class car(vehicle):
    "child class for cars"
    def __init__(self, make, model, color, fueltype, option, enginesize, numdoors):
        super().__init__(make, model,color,fueltype,option)
        self.enginesize =  enginesize         #input("Type in the engine size: ")
        self.numdoors= numdoors    # in the number of doors: ")

    def getenginesize(self):
        return self.enginesize

    def getnumdoors(self):
        return self.numdoors

    def display_info(self):
        super().display_info()
        print(f"Engine size: {self.enginesize}, Number of doors:{self.numdoors}")

class pickup(vehicle):
    "child class for trucks"
    def __init__(self, make, model, color, fueltype, option, cabStyle,
                 bedLength):
            super().__init__(make, model,color,fueltype,option)
            self.cabStyle= cabStyle         #input("Type in the Cab Style: ")
            self.bedLength=   bedLength     #input("Type in the Bed Length: ")

    def getcabStyle(self):
        return self.cabStyle

    def getbedLength(self):
        return self.bedLength

    def display_info(self):
        super().display_info()
        print(f"Cab Style: {self.getcabstyle()}, Bed Length:{self.getbedlength()}")


def printGarageMenu():
    print("Welcome to Steve's Virtual Garage Builder Menu")

    print("[1] Choose a Car")
    print("[2] Choose a Pickup")
    print("[3] Display your Vehicles")
    print("[4] Quit")

    return int(input("Please select an option from the menu:"))

def showGarage():
    print("This should display your vehicles", pickup(car.getmake(), pickup.getmodel(), pickup.getcolor(), pickup.getfueltype(), pickup.getoption() ,pickup.getenginesize(), pickup.getnumdoors()))
    print("This should display your vehicles", pickup(car.getmake(), pickup.getmodel(), pickup.getcolor(), pickup.getfueltype(), pickup.getoption() ,pickup.getenginesize(), pickup.getnumdoors()))

def main():
    option_choices = {'1':'Power Mirrors' , '2':'Power locks' , '3':'Remote Start' ,
           '4': 'Backup Camera', '5':'Bluetooth' ,'6': 'Cruise control' ,
           '7':'Assisted steering' ,'8': 'Autopark' }
    garage = []
    while (True):
        garageOption = printGarageMenu()

        if garageOption == 1:
            car.make = input("Please type in a car manufacturer: ")
            car.model = input("Please type in a car model: ")
            car.color = input("Please type in a car color: ")
            car.fueltype = input("Please type in a fuel type: ")
            print ("The following are a list of options for your vehicle", option_choices)
            car.option = input("Please choose one the options using the applicable number: ")
            if car.option in option_choices:
                print (car.option, option_choices.get(car.option))
            else:
                print ("That was not a valid choice, please try again: ")            
            car.enginesize = input ("Please type an engine size: ")
            car.numdoors = input ("Please type the number of doors available: ")
            garage.append(car)

        elif garageOption == 2:
            pickup.make = input("Please type in a pickup manufacturer: ")
            pickup.model = input("Please type in a pickup model: ")
            pickup.color = input("Please type in a pickup color: ")
            pickup.fueltype = input("Please type in a fuel type: ")
            print ("The following are a list of options for your vehicle", option_choices)
            pickup.option = input("Please choose one the options using the applicable number: ")
            if pickup.option in option_choices:
                print (pickup.option, option_choices.get(pickup.option))
            else:
                print ("That was not a valid choice, please try again: ")            
            pickup.cabStyle = input ("Please type a cab style: ")
            pickup.bedLength = input ("Please type the length of the truck bed: ")
            garage.append(pickup)

        elif garageOption == 3:
            if (len(garage) == 0):
                print("You have no vehicles in the garage.")
            else:
                showGarage(garage)

        elif (garageOption == 4):
             print("Thanks for using the virtual garage builder.")
             break

        else:
            print("Invalid option, please try options 1 through 4:")

   
main()


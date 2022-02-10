
class vehicle(object):
    "Parent class for vehicle features and options"
    def __init__ (self, make, model, color, fueltype, options):
        self.make = make          #input("Type in a car manufacturer ")
        self.model = model           #input("Type in a car model ")
        self.color =  color          #input("Type in a car color ")
        self.fueltype = fueltype        #input("Type in a car fuel type ")
        self.options =  options         #input("Type in a car option ")
        
    def getmake(self):
        return self.make

    def getmodel(self):
        return self.model

    def getcolor(self):
        return self.color

    def getfueltype(self):
        return self.fueltype

    def getoptions(self):
        return self.options
    
    def display_info(self):
        #return '{} {} {} {} {}'.format(self.make, self.model, self.color, self.fueltype, self.options)
        print (f"You have a {self.make} {self.model} and it is {self.color} and has {self.options}")

class car(vehicle):
    "child class for cars"
    def __init__(self, make, model, color, fueltype, options, enginesize, numdoors):
        super().__init__(make, model,color,fueltype,options)
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
    def __init__(self, make, model, color, fueltype, options, cabStyle,
                 bedLength):
            super().__init__(make, model,color,fueltype,options)
            self.cabStyle= cabStyle         #input("Type in the Cab Style: ")
            self.bedLength=   bedLength     #input("Type in the Bed Length: ")

    def getcabStyle(self):
        return self.cabStyle

    def getbedLength(self):
        return self.bedLength

    def display_info(self):
        super().display_info()
        print(f"Cab Style: {self.getcabstyle()}, Bed Length:{self.getbedlength()}")

option_choices = {'Option 1':'Power Mirrors' , 'Option 2':'Power locks' , 'Option 3':'Remote Start' ,
           'Option 4': 'Backup Camera', 'Option 5':'Bluetooth' ,'Option 6': 'Cruise control' ,
           'Option 7':'Assisted steering' ,'Option 8': 'Autopark' }

#Testing
#car1=car('Ford','Mustake', 'Pink','Gas Guzzler','Bluetooth','BigMotor','4 Door')
#print (car1.getmake(), car1.getmodel(), car1.getcolor(), car1.getfueltype(), car1.getoptions() ,car1.getenginesize(), car1.getnumdoors())
#truck1= pickup('Chevy','Silverado', 'Blue', 'Diesel', 'CruiseControl','Crew','ShortBox')
#print (truck1.getmake(), truck1.getmodel(), truck1.getcolor(), truck1.getfueltype(),truck1.getoptions(),truck1.getcabStyle(), truck1.getbedLength())


print ("Please type 1 for a car, and 2 for a pickup ")
x = int(input())
While x == or x == 2:
        break;
    else:
         print("Please try again to select a vehicle, 1 for car, 2 for pickup")
    except ValueError:
        print ("please enter the number one or two")
        continue
if x == 1:
    #get car attributes#(car.getmake(), car.getmodel(), car.getcolor(), car.getfueltype(), car.getoptions() ,car.getenginesize(), car.getnumdoors())
    car1 = car()
    car1.make = input("Please type in a car manufacturer: ")
    car1.make = input("Please type in a car model: ")
    car1.color = input("Please type in a car color: ")
    car1.fueltype = input("Please type in a fuel type: ")
    print (option_choices)
    car1.options = input("Please choose one the options using the appropriate number: ")
    car1.enginesize = input ("Please type an engine size: ")
    car1.numdoors = input ("Please type the number of doors available: ")
    print (car1.getmake(), car1.getmodel(), car1.getcolor(), car1.getfueltype(), car1.getoptions(option_choices.get()) ,car1.getenginesize(), car1.getnumdoors())

elif x == 2:
    #get truck attributes
    pickup1 = pickup()
    pickup1.make = input("Please type in a car manufacturer: ")
    pickup1.make = input("Please type in a car model: ")
    pickup1.color = input("Please type in a car color: ")
    pickup1.fueltype = input("Please type in a fuel type: ")
    print (option_choices)
    pickup1.options = input("Please choose one the options using the appropriate number: ")
    pickup1.cabStyle = input ("Please type the cab style: ")
    pickup1.bedLength = input ("Please type the bed size: ")
    print (pickup1.getmake(), pickup1.getmodel(), pickup1.getcolor(), pickup1.getfueltype(), pickup1.getoptions(option_choices.get()) ,pickup1.getcabStyle(), car1.getbedLength())



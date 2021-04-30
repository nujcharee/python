class Car(object):
    
    """
    Class Car is the parent class.
    It has a string object "condition" with initial value "New"
    
    Attributes
    ----------
    model  : model of the car e.g Honda, Suzuki, Vauxhall.
    colour : color of the car e.g Yellow, Blue, White, Black.
    speed  : speed of car in miles per hours unit.
    mpg    : miles per gallon.
    
    
    Methods
    -------
    display_car
        Prints a string which reads "This is a [colour] [model] with [mpg] MPG".
        
    drive_car
        Prints a string which reads "used".
    
    calculate_stopping_distance
        Returns a float object which calculates stopping distance.
    
    """
    condition = "New"
    
    def __init__(self, model = None, colour = None, speed = None, mpg=None):
       
        """ 
        Constructor that initiate Car class 

        """
    
        self.model = model
        self.colour = colour
        self.speed = speed
        self.mpg = mpg 
        
        
    
    
    def setModel(self, model = None)->str:
        
        """
        Validation rules:
        ----------------

        * A user can not enter in more than 32 characters
        * A user can not enter in an empty string or whitespace

        """
        
        while True:
            model = input("Enter model: ")
            
            try:

                model == str(model)
                
                # Valid conditions
                if len(model)<=32:
                    self.model = model
                    break;
                
                # Invalid conditions
                if not model:
                    print('Please enter car model, dont leave it blank: ')
                    continue
                if model.isnumeric():
                    print("Cant be number.")
                    continue

                if len(model)>32:
                    print("Thats a very long name for a car!")
                    continue
                
                else:
                    print("Please retry")
                    continue

            except ValueError as Err:
                print(Err)
    

        
    def setColour(self, colour = None)-> str:
        
        colour_list = ['YELLOW','BLUE', 'BLACK', 'WHITE', 'RED']
        
        while True:
        
            try:
                colour = str(input("Enter car colour: ")).upper()
                
                if colour in colour_list:
                    print("Nice colour!")
                    self.colour = colour
                    break;    
                else:
                    print("Choose from following options: ['Yellow', 'Blue', 'Black', 'White', 'Red']")
            except ValueError as e:
                    print("Please retry")
                    continue
    
    def setSpeed(self, speed=0)->float:
        
        """
        Validation rules:
        ----------------

        * A user can not enter other data type but number.
        * A user can not enter negative number.
        * A user can not enter zero.
        * A user can not enter number greather than 61.


        * A user can only enter range from 1-60

        """
        
        while True:
            speed = input("Enter speeds MPH (between 1-60)): ")
            try:
                speed = float(speed)
                
                # Valid conditions
            
                if  speed > 0 and speed <= 60 : # normal range https://en.wikipedia.org/wiki/0_to_60_mph
                    self.speed = speed
                    break;
                    
                # Invalid conditions
                
                if speed < 0:
                    print("Speed cannot be negative")
                    continue
                if speed == 0:
                    print("It appears you aren't moving right now?")
                
                if 61 <= speed <= 99:
                    print("Impressive speed!!! Normal range is greater than 0 up to 60 (mph).")
                    continue
                if 100 <= speed <= 200:
                    print("You must owe some sort of Formula 1 car!, normal range is greater than 0 up to 60 (mph).")
                    continue
                if speed > 200:
                    print("Seems unrealistically high! Normal range is greater than 0 up to 60 (mph).")
                    continue 
            except ValueError:
                print('Speed must be number')
                continue
            else:
                print("Please retry")
                continue

        
    def setMPG(self, mpg=0)->float:
        
        """
        Validation rules:
        ----------------

        * A user can not enter other data type but number.
        * A user can not enter negative number.
        * A user can not enter zero.
        * A user can not enter number greather than 61.


        * A user can only enter range from 1-60

        """
        
        while True:
            mpg = input("Enter MPG (max 60): ")
            
            try:
                mpg = float(mpg)
            except ValueError:
                print('Speed must be number')
                continue
            
            if  mpg > 0 and mpg <= 60 : # normal range https://en.wikipedia.org/wiki/0_to_60_mph
                self.mpg = mpg
                break;
                
            if mpg < 0:
                print("Speed cannot be negative")
                continue
            if mpg == 0:
                print("Car with no MPG information, thats not right?")
            if 61 <= mpg <= 100:
                print("Impressive MPG!!! Highest MPG in our record is 60.")
                continue
            if 100 <= mpg <= 200:
                print("You must owe some sort of Formula 1 car!, Highest MPG in our record is 60.")
                continue
            if mpg > 200:
                print("Seems unrealistically high! Highest MPG in our record is 60.")
                continue 
            else:
                print("Please retry")

    
    def getModel(self):
        return self.model
    
    def getColour(self):
        return self.colour
        
    def getSpeed(self):
        return self.speed
        
    def getMPG(self):
        return self.mpg
        
    def display_car(self):
        
        """
        Returns
        -------
        a string that return attributes of the car which reads "This is a [colour] [model] with [mpg] MPG".
        
        """
        print("\n-----------------------------------")
        print("This is a %s %s with %s MPG." % (self.colour, self.model, self.mpg))
    
    def drive_car(self)->str:
        
        """
        Returns
        -------
        a string that return the car condition that reads "Used".
        
        """
    
        self.condition = "Used"
        return self.condition  
    
    def calculate_stopping_distance(self, speed: float)->float:

        
        """
        Parameters
        ----------
        
        speed  : speed of car in miles per hours unit.
        
        Returns
        -------
        a float that returns calculated stopped distance in meter per second (m/s).
        
        
        Raises
        ------
        KeyError
        when a key error is triggered, users are prompted with an input box to re-enter value.
            
            
        """
        
        # Initialise variables
        
        self.speed = speed
        
        """
        TR     : reaction time in seconds (s). The average reaction time of 1.5 (s) is used in the calculations
        G      : gravitational acceleration, fixed value at 9.81.
        
        """
        
        TR = 1.5
        G = 9.81
        
        # To convert the speed of the car from miles per hour (mph) 
        # to meter per second (m/s)  
        
        v_m_s =  self.speed / 2.237 
        
        
        """ Possible weather conditions to choose from """
        friction_dict = {"DRY": 0.7,"WET": 0.5,"ICY": 0.3}
        
        
        """
        Validation rules:
        ---------------- 
        * user can only choose weather conditions from options above.
        
        """
        
        while True:
            try:
                self.friction = friction_dict[input("Enter weather condition [Dry, Wet, Icy]: ").upper()]
                
                break;
            except KeyError:
                print("Choose from following options: [Dry, Wet, Icy]")


        """
        Retrieve mu value from friction dictionary
        Calculate BD (braking distance) 
        Calculate RD (reaction time in meter per second)
        Calculate SD (Stopping Distance)
        
        """
        
        mu = self.friction
        
        # Braking Distance Calculation
        BD = (v_m_s**2)/(2*mu*G)
        
        # Reaction time in meter per second
        RD = v_m_s * TR
        
        # Stopping Distance Calculation

        SD = RD + BD 
        # Return SD
        print("\n-----------------------------------")
        print("Stopping distance is {0:.{1}f}".format(SD,2),  " meters.")
        print("-------------------------------------")

    
    def DisplayMenu(self):
        
        print("\n*********************************")
        print("***** Welcome to OOP Car Sales ****")
        print("*********************************")
        print("1. Enter Car Specifications")
        print("2. View used cars")
        print("Q. Quit")
        print("\nEnter your choice: ", end = "")
    
    def Run(self):
        Choice = ""
        
        while Choice != "Q":
            self.DisplayMenu()
            Choice = str(input()).upper()
            if Choice == "1":
                self.setModel()
                self.setColour()
                self.setSpeed()
                self.setMPG() 
                print("")
                print("-------------------------------------")
                print("Specifications entered: ")
                print("Thank you!")
                self.display_car()
                print("Condition: ", self.condition)
                print("-------------------------------------")
                
                print("Base on given speed, I can calculate stopping distance!")
                self.calculate_stopping_distance(self.speed)
                print("-------------------------------------")

            elif Choice == "2":
                print("-------------------------------------")
                print("This is a %s %s with %s MPG." % (self.colour, self.model, self.mpg))
                print("Condition: ", self.drive_car())
                print("-------------------------------------")
                
            elif Choice == "Q":
                print("Thank you, come back again soon.")
                print("press Enter to close.")
                input()
            else:
                print("Only choose from the option above!!!!")

class ElectricCar(Car):
    
    """
    ElectricCar class inherits from Car class.
    
    Attributes
    ----------
    battery_type  : a string that describes type of battery.
    
    
    Methods
    -------
        
    drive_car
        Prints a string which reads "less than three years old.".
    
    """
    
    
    def __init__(self, model = None, colour = None, speed = None, mpg=None, battery_type=None):

        super().__init__(model, colour, speed, mpg)
        self._battery_type = battery_type
    
       
    def setBatteryType(self, battery_type=None)->str:
        
        
        battery_list = ["LITHIUM ION BATTERY", "NICKEL-METAL HYDRIDE", "DONT KNOW"]
        
        while True:
        
            try:
                battery_type = str(input("Enter battery type: ")).upper()
                
                if battery_type in battery_list:
                    self.battery_type = battery_type
                    break;    
                else:
                    print("[LITHIUM ION BATTERY, NICKEL-METAL HYDRIDE, DONT KNOW]")
                    print("Choose from these options: ")
            except ValueError as e:
                    print("Please retry")
                    continue

        
    def getBatteryType(self)->str:
        return self.battery_type
  
    def drive_car(self)->str:
        
        Car.drive_car(self)
        Car.condition = "less than three years old."
        return Car.condition
    
    def RunElectric(self):
        
        self.setBatteryType()
        print("")
        print("Searching for a car that meets specs.................")
        Car.display_car(self)
        print("Battery Type: ", self.getBatteryType())
        print("Condition: ", self.drive_car())

class PetrolOrDieselCar(Car):
    """
    Petrol or Diesel class inherits from Car class.
    
    Attributes
    ----------
    fuel_type  : a string that describe type of fuel.
    
    
    Methods
    -------
        
    drive_car
        Prints a string which reads "less than three years old.".
    
    """
    def __init__(self, model = None, colour = None, speed = None, mpg=None, fuel_type=None):
        super().__init__(model, colour, speed, mpg)
        self.fuel_type = fuel_type


    def setFuelType(self, fuel_type=None):
        
        fuel_choice = ['PETROL','DIESEL']
        
        while True:
        
            try:
                fuel_type = input("Choose fuel type: ").upper()
                
                if fuel_type in fuel_choice:
                    break;    
                else:
                    print("Choose from following options: ['PETROL','DIESEL']")
            except ValueError as e:
                    print("Please retry")
                    continue
                  
    
        self.fuel_type = fuel_type
        
        
    def getFuelType(self):
        return self.fuel_type
  
    def drive_car(self):
        Car.drive_car(self)
        Car.condition = "less than three years old."
        return Car.condition
    
    def RunPetrolDiesel(self):
        self.setFuelType()
        print("Searching for a car that meets specs.................")
        print(".....................................................")
        Car.display_car(self)
        print("Battery Type: ", self.getFuelType())
        print("Condition: ", self.drive_car())

def subMenu():
    
    print("\n*********************************")
    print("*****    OOP Car Show Rooms   ****")
    print("*********************************")
    print("1. Electric Stocks")
    print("2. Petrol / Diesel Stocks")
    print("Q. Quit")
    print("\nEnter your choice: ", end = "")
        
def main():
    
    
    #initialise with default values

    mycar = Car("", "", 0, 0)
    mycar.Run()
    
    print("Before you go, let me show you our car stocks!!!")
    
    Choice = ""
    
    while Choice != "Q":
        subMenu()
        Choice = str(input()).upper()
        
        if Choice == "1":
            eCar = ElectricCar(mycar.getModel(), mycar.getColour(), mycar.getSpeed(), mycar.getMPG(), "")
            eCar.RunElectric()  
        elif Choice == "2":
            pd = PetrolOrDieselCar(mycar.getModel(), mycar.getColour(), mycar.getSpeed(), mycar.getMPG(), "")
            pd.RunPetrolDiesel()
        elif Choice == "Q":
            print("Thank you, come back again soon.")
            print("press Enter to close.")
            input()
        else:
            print("Only choose from the option above!!!!")
            
if __name__ == "__main__":
    main()

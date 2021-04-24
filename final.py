class Car(object):
    
    condition = "New"
    
    
    def __init__(self, model = None, colour = None, speed = None, mpg=None):
       
        self.model = model
        self.colour = colour
        self.speed = speed
        self.mpg = mpg 
    
    
    def setModel(self, model = None)->str:
        
        while True:
            model = input("Enter model: ")
            
            try:

                model == str(model)
                
                if not model:
                    print('Please enter car model, dont leave it blank: ')
                    continue
                if model.isnumeric():
                    print("Cant be number.")
                    continue

                if len(model)<=32:
                    self.model = model
                    break;
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
                    break;    
                else:
                    print("Choose from following options: ['Yellow', 'Blue', 'Black', 'White', 'Red']")
            except ValueError as e:
                    print("Please retry")
                    continue
    
    def setSpeed(self, speed=0)->float:
        
        while True:
            speed = input("Enter speeds MPH (between 1-60)): ")
            try:
                speed = float(speed)
            
                if speed < 0:
                    print("Speed cannot be negative")
                    continue
                if speed == 0:
                    print("It appears you aren't moving right now?")
                if  speed > 0 and speed <= 60 : # normal range https://en.wikipedia.org/wiki/0_to_60_mph
                    self.speed = speed
                    break;
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
        
        while True:
            mpg = input("Enter MPG (max 60): ")
            try:
                mpg = float(mpg)
            except ValueError:
                print('Speed must be number')
                continue
            if mpg < 0:
                print("Speed cannot be negative")
                continue
            if mpg == 0:
                print("Car with no MPG information, thats not right?")
            if  mpg > 0 and mpg <= 60 : # normal range https://en.wikipedia.org/wiki/0_to_60_mph
                self.mpg = mpg
                break;
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
        a string that return the car condition that reads "used".
        
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
        tr     : reaction time in seconds (s). The average reaction time of 1.5 (s) is used in the calculations
        g      : gravitational acceleration, fixed value at 9.81.
        
        """
        self.g = 9.81
        self.tr = 1.5
        
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
        BD = (v_m_s**2)/(2*mu*self.g)
        RD = v_m_s * self.tr

        SD = RD + BD 
        #return SD
        print("\n-----------------------------------")
        print("Stopping distance is {0:.{1}f}".format(SD,2),  " meters.")
        print("-------------------------------------")

    
    def DisplayMenu(self):
        
        print("\n*********************************")
        print("**********    MENU     **********")
        print("*********************************")
        print("1. Enter Car Information")
        print("2. Display Car")
        print("3. Check condition")
        print("4. Calculate Stopping Distance")
        print("Q. Quit")
        print("\nEnter your choice: ", end = "")
    
    def Run(self):
        Choice = ""
        
        while Choice != "Q":
            self.DisplayMenu()
            Choice = str(input())
            if Choice == "1":
                self.setModel()
                self.setColour()
                self.setSpeed()
                self.setMPG() 
                print("")
                print("-------------------------------------")
                print("Car information entered.")
                print("Select option 2 to review.")
                print("-------------------------------------")
            elif Choice == "2":
                self.display_car()
                print("Current condition: ", self.condition)
                print("-------------------------------------")

            elif Choice == "3":
                print("-------------------------------------")
                self.drive_car()
                print("After condition: ", self.condition)
                print("-------------------------------------")
                
            elif Choice == "4":
                print("-------------------------------------")
                self.calculate_stopping_distance(self.speed)

            elif Choice == "Q":
                print("Simulation finished, press Enter to close.")
                input()

def main():

    mycar = Car("", "", 0, 0)
    mycar.Run()

if __name__ == "__main__":
    main()
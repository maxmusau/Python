# class definition
class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    # define the methods/functions in the class
    def Start_engine(self):
        print(f"{self.brand} {self.model} Started")
    def Stop_engine(self):
        print(f"{self.brand} {self.model} Switched off")
# object instantiation
my_car=Car("Mazda", "CX 5", "2000")

# access the object attributes
print(my_car.brand)
print(my_car.model)
print(my_car.year)

# accessing the functions /object methods
my_car.Start_engine()
my_car.Stop_engine()

# inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, year,batteryCapacity):
        super().__init__(brand, model, year) #Car is the super class
        self.batteryCapacity=batteryCapacity
        # methods 
    def ChangeBattery(self):
        # calling functions from super class
        super().Start_engine()
        new_capacity="35KWh"
        print(f"{self.brand} {self.model} \n old battery capacity= {self.batteryCapacity} \n new capacity= {new_capacity}")
        super().Stop_engine()
    
# create an object
my_electric_car=ElectricCar("Toyota", "Harrier", 2010, "30KWh")
# access the attributes
print(my_electric_car.batteryCapacity)

# calling the function
my_electric_car.ChangeBattery()

# method overiding
class SportsCar(Car):
    #TODO
    def Start_engine(self):
        print("Start Engine  for Sportscar")
my_sportscar=SportsCar("Ferrari", "488 GTB", 1998)
my_sportscar.Start_engine()


# bank account
# balance
# agent_number

# check if user 
# 8 digits
# 100 
# 4 digits, numbers(int)



# Encapsulation
# redo the ussd program using object oriented programming and apply Encapsulation
# Read on Flask Framework
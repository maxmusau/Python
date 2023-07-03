# modules
from Lesson7a import *

# parameters-are passed inside the parenthesis when defining a function
# arguments - values passed inside the parenthesis when calling the functionn
def Name(name): #name is a parameter
    print(f"My name is {name}")
Name(name="Maxwell")
Name("Yuri") #Yuri is an argument 

# function to calculate BMI
def BMI(name,weight,height):
    BMI=weight/height**2
    greetings()
    print(f"{name} has a BMI value of {BMI}")
BMI(weight=70,height=1.7,name="Faith") #positional arguments
BMI("Mayar", 65, 1.6) #default arguments



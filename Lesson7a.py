# function is a block of code that performs a specific task
# python functions are defned using keyword def
# syntax  def function_name():
# we use parenthesis() next to the function_name when defining the functions
# to execute the code in the  function we must call the function e.g function_name()
#len()
# user-defined functions
# a function that prints greetings

def greetings():
    print("Hello There")
# call the function
greetings()

# function that adds two numbers
def addition():
    num1=30
    num2=40
    print(num1+num2)
addition()

# function that prints the detais of a student
def stdudent():
    name=input("Enter Name: ")
    DOB=input("Enter DOB: ")
    Course=input("Enter Course name:   ")
    Reg_no=input("Enter Registration number: ")
    Campus=input("Enter University name: ")
    print(f"Student name = {name} \n Date of Birth = {DOB} \n Course = {Course} \n Registration number= {Reg_no} \n Campus = {Campus}")
stdudent()
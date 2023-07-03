# create a function to check the largest number given 3 numbers. 
# define the 3 numbers as parameters
def Largest(num1,num2,num3): #parameters
    if num1>num2:
        if num1>num3:
            print(f"{num1} is the largest")
        else:
            print(f"{num3} is the largest")
    elif num2 >num3:
        print(f"{num2} is the largest")
    else:
        print(f"{num3} is the largest")
Largest(390, 70, 10) #arguments

# control flow
# conditional statements  =if, if..else, if..elif..else
# iterative statements =for loop, while loop

# conditional statements
# if

number=-3

print(number >0)
# check if number is positie or not
# if -one condition
# ith one option
if number >0:
    print(f"{number} is a positive number")
    
# check if number is positive or negative
# if..else - one condition with two options
if number >=0:
    print(f"{number} is a positive number or zero")
else:
    print(f"{number} is a negative number")

# if..elif..else -multiple conditions
if number >0:
    print(f"{number} is a positive number")
elif number ==0:
    print(f"{number} is equal to zero")
else:
    print(f"{number} is a negative number")

# create two variables of numbers
# check the bigger number
num1=20
num2=10
if num1>num2:
    print(f"{num1} is bigger than {num2}")
elif num1 == num2:
    print(f"{num1} is equal to {num2}")
else:
    print(f"{num2} is bigger than {num1}")
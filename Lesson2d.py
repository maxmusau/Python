# write a python program to calculate the simple interest
# formula: SI=P * R* T
SI=2300 *2 *2 /100
print(SI)


# BMI Body Mass Index
# formula BMI=weight / height**2
# using above formula , calculate the BMI value of person x
name=str(input("Enter name: "))
weight=int(input("Enter value of weight in Kgs: "))
height=float(input("Enter value of height in M: "))
BMI=weight / height**2
print(f"{name} who is {weight} kgs and {height}M tall has a BMI value of {BMI}")

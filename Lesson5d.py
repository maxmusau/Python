# Nested if statement
# if statements inside other if statment
# program to check if someone qualifies to donate blood
# age
# weight
age=int(input("Enter the age:  "))
weight=float(input("Enter weight in kgs: "))
bloop_p=input("Enter Blood pressure status: ")
if age >=18:
    if weight >=50:
        # check for another condition
        if bloop_p =='True':
            print("Qualifies without complications")
        else:
            print("Qualifies to donate blood with complications")   
    else:
        print("Do not Qualify : Underweight")
else:
    print("Do not qualify: Underage")       
    

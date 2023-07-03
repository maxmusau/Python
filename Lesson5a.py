# If statements
# make decisions based on some conditions
# comparison operators applied
# when the condition is true(satisfied) then the bodt of if is executed 
# elif tests multiple conditions

# check performance of students based on percentage 

percentage=int(input("Enter Marks in percentage:  "))
if percentage>=0 and percentage <40:
    print("Failed")
elif percentage >=40 and percentage <55:
    print("Fair")
elif percentage >=55 and percentage <65:
    print("Good")
elif percentage >=65 and percentage <=100:
    print("Exccellent")
else:
    print("Invalid Input")

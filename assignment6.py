# create a program to calculate student performance
# the program should accept student name and marks 
# loop the program 5 times
# check performance for 5 students
def program1():
    for student in range(1,6):
        name=input("Enter name: ")
        percentage=int(input("Enter Marks in percentage:  "))
        print("Student",student)
        if percentage>=0 and percentage <40:
            print("name= ",name)
            print("Percentage= ",percentage)
            print("Failed")
        elif percentage >=40 and percentage <55:
            print("name= ",name)
            print("Percentage= ",percentage)
            print("Fair")
        elif percentage >=55 and percentage <65:
            print("name= ",name)
            print("Percentage= ",percentage)
            print("Good")
        elif percentage >=65 and percentage <=100:
            print("name= ",name)
            print("Percentage= ",percentage)
            print("Exccellent")
        else:
            print("Invalid Input")
        
# while
count=1
while count <6:
    name=input("Enter name: ")
    percentage=int(input("Enter Marks in percentage:  "))
    print("Student",count)
    if percentage>=0 and percentage <40:
        print("name= ",name)
        print("Percentage= ",percentage)
        print("Failed")
    elif percentage >=40 and percentage <55:
        print("name= ",name)
        print("Percentage= ",percentage)
        print("Fair")
    elif percentage >=55 and percentage <65:
        print("name= ",name)
        print("Percentage= ",percentage)
        print("Good")
    elif percentage >=65 and percentage <=100:
        print("name= ",name)
        print("Percentage= ",percentage)
        print("Exccellent")
    else:
        print("Invalid Input")
    count=count+1
    print("\n") 
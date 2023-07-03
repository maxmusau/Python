# check if given number is even or odd
number=0
if number==0:
    print("Number is even (zero)")
elif (number % 2) ==0:
    print("Even number")
else:
    print("Odd number") 
    
# a program to accept 1-7 and display the day of the week
day=int(input("Enter day of the week: "))
if day==1:
    print(f"Day is {day} name is Monday")
elif day==2:
    print(f"Day is {day} name is Tuesday")
elif day==3:
    print(f"Day is {day} name is Wednesday")
elif day==4:
    print(f"Day is {day} name is Thurday")
elif day==5:
    print(f"Day is {day} name is Friday")
elif day==6:
    print(f"Day is {day} name is Saturday")
elif day==7:
    print(f"Day is {day} name is Sunday")
else:
    print("Invalid Input")
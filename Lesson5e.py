# python program to ckeck if year is leap year or not (366 days)
# leap year- divisible 4,
year=int(input("Enter the year: "))
if year % 4==0:
    # check if year divisible by 100
    if year% 100==0:
        # TODO
        # check if year divisible by 400
        if year % 400==0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap year")
else:
    print("Not a Leap Year")
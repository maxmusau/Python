# write a program that acceps 3 numbers. check the largest out of the three
# use nested if statements
num1=17
num2=100
num3=160
if num1>num2:
    if num1>num3:
        print(f"{num1} is the largest")
    else:
        print(f"{num3} is the largest")
elif num2 >num3:
    print(f"{num2} is the largest")
else:
    print(f"{num3} is the largest")
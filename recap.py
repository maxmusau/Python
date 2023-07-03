# create python program to accept height and weight of person x 
# apply if statements to output whether person is underweight (BMI <18.5), normalbetween 18.5 to 22.5, overweight (BMI >22.5)

height=1.9
weight=100
BMI=weight/(height*height)
if BMI<18.5:
    print(BMI)
    print("UNDERWEIGHT")
elif BMI >=18.5 and BMI<=22.5:
    print(BMI)
    print("NORMAL")
else:
    print(BMI)
    print("OVERWEIGHT")

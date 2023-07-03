countries={
'Kenya':{
'Presidents':['Ruto','Uhuru','Kibaki'],
'Vice President':'Rigathi'
},
'Uganda':{
'Presidents':['Yoweri Museveni','Tito Okello Lutwa','Milton Obote'],
'Vice President':'Jessica Alupo'
},
'USA':{
'Presidents':['Joe Biden','Donald Trump','Barack Obama'],
'Vice President':'Kamala'
}
}


# add another country
countries["Rwanda"]={
        "Presidents":['Kagame','President 2','president 3'],
        "Vice president":'Not Applicable'
    }
print(countries)

# empty
MyFamily={}
# print(MyFamily)
first_child={
    "Name":"Mike",
    "DOB":"12/6/2000",
    "School":"Aliance Boys"
}

second_child={
    "Name":"Mercy",
    "DOB":"13/5/2004",
    "School":"Precius blood Riruta"
}
MyFamily={
    "first_child":first_child,
    "Second_child":second_child
}
print(MyFamily)
print(MyFamily['Second_child']['Name'])

# Task 4
# program to calculate electricity bill
first_100=0
next_100=5
above_200=10
# input unit =350
# first 100-free
# 100*5=500
# 150*10=1500
units=350
if units <=100:
    total_fee=units*0
    print(f"Units = {units} \n Total_Fee= {total_fee}")
elif units >100 and units <=200:
    total_fee=100*0+(units-100)*5
    print(f"Units = {units} \n Total_Fee= {total_fee}")
elif units >200:
    total_fee=100*0+(100)*5+(units-200)*10
    print(f"Units = {units} \n Total_Fee= {total_fee}")
else:
    print("Invalid Input")

# BMI program
weight=160
height=1.9
BMI=weight /height**2
if BMI <18.5:
    print(f"BMI = {BMI} \n Underweight")
elif BMI >=18.5 and BMI <=22.9:
    print(f"BMI = {BMI} \n Normal")
elif BMI >22.9 and BMI <=24.9:
    print(f"BMI = {BMI} \n Overweight")
elif BMI >24.9 and BMI <=29.9:
    print(f"BMI = {BMI} \n Pre-Obese")
elif BMI >29.9 and BMI <=34.9:
    print(f"BMI = {BMI} \n Obese Class I")
elif BMI >35 and BMI <=39.9:
    print(f"BMI = {BMI} \n Obese Class II")
elif BMI >40:
    print(f"BMI = {BMI} \n Obese Class III")
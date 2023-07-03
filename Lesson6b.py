# while loop
# execute certain code as long as a condition is true
count=0
while count<10:
    print(count)
    # increment the valu of count
    count=count+1
    if count==5:
        print(count)
        break
    # or 
    #count+=

# continue
# continue skips the current iteration but continues with the loop
number=0
while number <10:
    number=number+1
    if number ==6:
        continue 
    print(f"number is {number}")
    
    # list
    countries=['Latvia','Belarus','Turkey','Malawi']
    count=0
    for country in countries:
        while count<3:
            print(country)
            count=count+1
        else:
            print("Finished")
print("\n")
# nested for loops
countries=['Latvia','Belarus','Turkey','Malawi']
colors=['Red','White',"Black",'green']
for country in countries:
    print(country)
    for color in colors:
        print(color)
# iterative statements for loop, while loop
# for loop- iterate through a collection
fruits =['Orange','Mango','pineapple']
for item in fruits: #item is a new variable that represents individual item in the list
    print(item) 

for item in fruits:
    print(fruits)

# range
for number in range(10):
    print("Looping", number)
    
print("\n")
# range with start and end point
for number in range(5,10):
     print("looping",number)
print("\n")
# range with step
for i in range(2,14,3):
    print("skipping 1 item",i)

# break 
for item in fruits:
    print(item)
    if item=="Mango":
        # print(item)
        break
    
# break the loop for range (5,20) if the number is 11
for number in range(5,20):
    print(number)
    if number ==11:
        break
print("\n")
# string
name="Modcom"
for letter in name:
    print(letter)
    if letter=='d':
        break
# create a multiplication table of number 5 (from 0,10)
for num in range(11):
    num1=5*num
    print(f'5 multiplied by {num} is equal to {num1}')
multiple=5
for num in range(0,11):
    print(f"{multiple} * {num} ={num*multiple}")                 
    
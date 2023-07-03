# error Handling
# Try and exceptdef error()
number=20
try: 
    diviision=number /0
    print("Division = ",diviision)
except:
    print("Program encountered an error")
    print("Division not posible")
    
try:
    number="60"
    number2="50"
    addition=number +number2
    print(f"Addition of {number} and {number2} is {addition}")
except:
    print("Addition not successful")
    print("You can add an Integer with string")
     
    
# boolean
user_input="Modcom@gmail.com"
from_db =["Max@gmail.com"]
try:
    if user_input in from_db:
        print("Signin successful")
    else:
        print("User does not exist")
    # if status ==True:
    #     print("Signin successful")
    # else:
    #     print("User does not exist")
except:
    print("User does not exist")
    print("Program encountered an error")

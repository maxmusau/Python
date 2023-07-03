# Modules
from Lesson7d import Withdraw
from Functions import *
# Withdraw(500)

import math
# squareroot of a number 
print(math.sqrt(64))

# generate a random number 
import random
number=random.randint(1, 10) #choose one random number from the given range
password=generate_random() #generate a password based on given conditions
list1=[12,34,5,676,87,9,7,5,545]
random.shuffle(list1)
print(list1)

print(password)
print(len(password))

# check the operating system
import platform
operating_system=platform.system()
print(operating_system)

# date and time
from datetime import datetime
current_time=datetime.now()
print(current_time)
# format the date and time
formated=current_time.strftime('%d-%m-%Y %H:%M:%S')
print(formated)

password=password_hash("user1234")
print(password)


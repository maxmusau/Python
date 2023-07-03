# Python Lists
# Lists are created using square brackets []
# individual items in alist can be accessed using python indexing
# Lists are mutable- Changeable -can be edited
# Items in a list can be deleted
# you can append new items to a list
numbers=[23,43,45,67,87,54,34]
print(numbers)

# access using index
first_item=numbers[0]
print(first_item)

print(numbers[1])

# Negative indexing
last_item=numbers[-1]
print(last_item)

print(numbers[-2])

names=['Raymond','Stacy','Ricky','Marion','Faith']
print(names)
print(type(names))

# change
names[1]='Keziah'
print(names)

# remove
names.remove('Ricky')
print(names)

# pop
names.pop(1)
print(names)

# clear
names.clear()
print(names)

# append items/add items
names.append('Ian')
print(names)

names.append('Mercy')
print(names)

# extend
new_names=['Kariuki','Chebet','Omwega']
print(new_names)
names.extend(new_names)
print(names)

# allows duplicate entries
names.append('Chebet')
print(names)

# delete
# del names
# print(names)

# list constructor
languages=list(('Kotlin','HTML','Python','Javascript','Java'))
print(languages)
print(type(languages))

# sorting
numbers=[23,43,45,67,87,54,34]
numbers.sort()
print(numbers)

sorted(numbers)

# reverse
# numbers.sort(reverse=True)
print(numbers)

sorted(numbers)
print(numbers)

vowels=['a','c','b','g','d','f']
print(vowels)

vowels.sort()
print(vowels)
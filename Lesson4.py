# dictionaries
# created using curly braces {}
# its items are in form of key and value (pairs)
# mutable- add, modify, remove 
# does not allow duplicates
# unordered
car={
    'Name':'Subaru',
    'Model':'Impreza',
    'Milage':"50,000 km",
    'YOM':1980,
    'Model':'Forester'
}
print(car)
print(type(car))

# use key to access the values
print(car['Name'])
print(car['YOM'])

# access all  the keys
print(car.keys())

# access all the values
print(car.values())

# access items using items method
print(car.items())

# mutable
# add
car['color']='Blue'
print(car)

# modify
car['YOM']=2000
print(car)

# remove
# pop method
car.pop('Milage')
print(car)

# popitem -removes the last item from the dictionary
car.popitem()
print(car)

# del keyword
del car['Model']
print(car)

# add items
car['Colors']=[['Sky blue','Dark blue'],'Yellow','Red','Black']
print(car)
# print the first color (blue) 
print(car['Colors'][0][1])

# Nested dictionary
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
print(countries)
# access items
print(countries['USA']['Presidents'][2])
# print(countries['USA'])

# add another country to the nested dictionary above
# create two dictionaries and add them to  another(an empty) dictionary
# Tuple
# created using round brackets ()
# can be accessed using index /ordered
# unchangeable
# allow duplicate entry
countries=('Kenya','Uganda','Tanzania','Ghana','Zambia','Uganda')
print(countries)

# type
print(type(countries))

first_coutry=countries[0]
print(first_coutry)
# negative indexing
first_coutry=countries[-1]
print(first_coutry)

# immutable/unchangeable

# duplicates
print(countries)

# tuple constructor
cities=tuple(('Nairobi','New york','Nakuru','Mombasa'))
print(cities)
print(type(cities))

# change the tuple above to a list
cities=list(cities)
print(cities)
print(type(cities))

# chnage back to tuple
cities=tuple(cities)

tuple1=('item1',)
print(type(tuple1))

# check the length
print(len(tuple1))
print(len(cities))

tuple2=(True,'Glory',45,12.5,7j+3,[0,2,3,'Union'])
print(tuple2)
print(type(tuple2))

# joining two tuples
new_tuple=cities + tuple1
print(new_tuple)

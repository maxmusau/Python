# set
# created using curly braces
counties={'Nairobi','Machakos','Tharaka Nithi','Uasin Gishu','Siaya','Bomet','Tharaka Nithi'}
print(counties)
print(type(counties))

# set is not 
# does not accept duplicates
# add
counties.add('Kiambu')
print(counties)

# clear
counties.clear()
print(counties)

counties.add('Kiambu')
print(counties)

# data types
# set does not accept list-type items
set1={'Oranges',34,45,56.9}
# set2={['Roy',758,False]} 
print(set1)
# print(set2)

# constructor
set3=set(('Fast and Furius','The Old Guard','The Karate Kid'))
print(type(set3))
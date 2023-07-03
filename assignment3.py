# 1.
# crate an empty list 
# append two of your favourite movie actors 
# 2.
# create a nested list of colors
#3.
# join two sets
# 4
# convert the actors' list into a tuple

actors=[]
print(type(actors))
actors.append('Jason Bourne')
actors.append('Bruce Willis')
print(actors)

# nested list is a list inside another list
colors=['White',[['color 1','color2','color 3'],'Sky blue','Navy Blue','Dark blue'],'Yellow','Red']
print(colors)
print(colors[1][0][2])

# union
set1={1,2,3,4}
set2={'First','second','third'}
set1=set1.union(set2)
print(set1)

# convert list into a tuple
actors=tuple(actors)
print(type(actors))

# access the first three items in a list
# access list items from the third one to the 5th
# read on dictionaries
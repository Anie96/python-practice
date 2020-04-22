#create with set()
empty_set = set()
print(empty_set)

# {} does not create empty set
#creates empty dictionary instead cos dictionary came first in python
am_i_set = {}
print(type(am_i_set))
#create with curly brackets

even_numbers = {0, 2, 4, 6, 7, 8}
print(even_numbers)

#convert iterable with set()
#it basically converts list,tuple or dict to set
#it discards duplicate values
new_set = set('letters')
print(new_set)

from_list = set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'])
print(from_list)


#uses just the keys
from_dictionary = set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'})
print(from_dictionary)
#Various ways of creating a list

#create an empty list
empty_list = []
#print to console
print(empty_list)

#create list of strings(days)
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
#print to console
print(weekdays)

#create random list
weekdays = ['Something Random', {"groundhog": "Phil"}, "Feb. 2"]
#print to console
print(weekdays)


#create with list()
another_empty_list = list()
print(another_empty_list)

#convert string with list()
string_to_list = list('dog')
print(string_to_list)

#convert tuple with list() function
a_tuple = ('ready', 'or', 'not')
tuple_to_list = list(a_tuple)
print(tuple_to_list)

#create from string with the String.split() function
sample_string = '16/04/2020'
string_to_list = sample_string.split('/')
print(string_to_list)

#if string has more than one seperator
# it prints out empty string as one of the list items
another_sample_string = 'a/b//c/d///e'
another_string_to_list = another_sample_string.split('/')
print(another_string_to_list)

#get value from list by specifying offset
first_value = another_string_to_list[0]
print(first_value)

#you can also specify negative value
last_value = another_string_to_list[-1]
print(last_value)

#specify an index before start index or after end leads to IndexError
# value_after_end = another_string_to_list[9]
# print(value_after_end)

# value_before_start = another_string_to_list[-9]
# print(value_before_start)

#get item with a slice
marxes = ['Groucho', 'Chico', 'Harpo']
first_slice = marxes[0:2]
print(first_slice)

#you can stop with values other than one
step_slice = marxes[::2]
print(step_slice)

#slice with negative stop
negative_step_clice = marxes[::-2]
print(negative_step_clice)

#to reverse a list without mutating
list_reverse_slice = marxes[::-1]
print(list_reverse_slice)

#to reverse a list while by changing original list
#it changes the list but doesn't return its value
# marxes.reverse()
# print(marxes)

#slice with invalid index will return index or snap to nearest value
invalid_index_slice = marxes[4:]
print(invalid_index_slice)
another_invalid_slice = marxes[-6:]
print(another_invalid_slice)

#add item to end of list with append

marxes.append('Another One')
print(marxes)

#add item by offset with insert
marxes.insert(0, 'At Beginning')
print(marxes)

#insert at end
marxes.insert(6, 'At End')
print(marxes)

#duplicate all items with *

duplicate_marxes = marxes * 2
print(duplicate_marxes)

#merge list into another
#using extend()
new_list = ["I Am", "Another List"]
marxes.extend(new_list)
print(marxes)

#using +

another_new_list = ["Another List", "Again"]
marxes += another_new_list
print(marxes)


#Updating a List
#by offset
marxes[2] = "Changed Item"
print(marxes)

#with slice
marxes[4:6] = [1, 2]
print(marxes)
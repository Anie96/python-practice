
marxes = ['Groucho', 'Chico', 'Harpo']
#get value from list by specifying offset
first_value = marxes[0]
print(first_value)

#you can also specify negative value
last_value = marxes[-1]
print(last_value)

#specify an index before start index or after end leads to IndexError
# value_after_end = marxes[9]
# print(value_after_end)

# value_before_start = marxes[-9]
# print(value_before_start)

#get item with a slice

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


#get items index by value with index method

groucho_index = marxes.index('Groucho')

print(groucho_index)

#value not exist 
# index = marxes.index('Available')
# print(index)
#returns Value Error: Value not in list

#check if value exist in list 
is_groucho_present = 'Groucho' in marxes
print(is_groucho_present)
is_av_present = 'Available' in marxes
print(is_av_present)


#count occurence of value with count method

print(marxes.count('Harpo'))
print(marxes.count('Bob'))


#convert list to string with join()

print(' '.join(marxes))


#get length with len()
print(len(marxes))



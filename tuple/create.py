#tuple creation

empty_tuple = ()
print(empty_tuple)


#tuple with one element
#element must be followed by , to make a tuple 
#if not you just get the thing/object back
one_element_tuple = ('First',)
print(one_element_tuple)

#tuple with more than one element
many_elemts_tuple = ('Groucho', 'Chico', 'Harpo')
print(many_elemts_tuple)

#can also create without parenthesis

without_parenthesis = 'Groucho',
print(type(without_parenthesis))
#You ccant pass into as an argument to a function
print(type('Groucho',))


#tuple unpacking
#almost similar to destructuring in js
marx_tuple = ('Groucho', 'Chico', 'Harpo')
a, b,c = marx_tuple
print(a)
print(b)
print(b)

#to swap values in one statement without tmp variable 
first = '2'
second = '4'
print(first, second)
first, second = second, first
print(first, second)


#create with tuple()
marx_list = ['Groucho', 'Chico', 'Harpo']
print(tuple(marx_list))


#Combine tuples with +

combined_tuple = ('Groucho',) + ('Second', 'Third')
print(combined_tuple)

#Duplicate items with *

duplicate_tuple = ('duplicate me ') * 4
print(duplicate_tuple)

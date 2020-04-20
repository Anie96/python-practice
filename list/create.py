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

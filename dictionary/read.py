non_empty_dict = {"one": ["first", "second"], "two": ["third", "fourth"]}


# get item by key
first_element = non_empty_dict["one"]
print(first_element)

# get with dictionary.get()
second_value = non_empty_dict.get("two")
print(second_value)

# define a value to return when key isn't present
# throws a key-error if its not defined
value_not_present = non_empty_dict.get("third", "Key not present")
print(value_not_present)

# get all keys with dictionary.keys()
# it returns an iterable type dict_keys
# returns a list of the keys in python2
all_keys = non_empty_dict.keys()
print(all_keys)
print(type(all_keys))


# get all keys with dictionary.values()
# it returns an iterable type dict_values
all_values = non_empty_dict.values()
print(all_values)
print(type(all_values))


# get all items with dictionary.items()
# it returns an iterable type dict_items
all_items = non_empty_dict.items()
print(all_items)
print(type(all_items))


#get length with len()

length = len(non_empty_dict)
print(length)


#check presense in in
print("one" in non_empty_dict)

print("three" in non_empty_dict)
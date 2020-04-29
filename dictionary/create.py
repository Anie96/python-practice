# empty dictionary with {}

empty_dictionary = {}
print(empty_dictionary)


second_empty = dict()
print(second_empty)
# non-empty dictionary
# keys must be immutable types
# values can be mutable or mutable

non_empty_dict = {1: ["first", "second"], 2: ["third", "fourth"]}
print(non_empty_dict)

# with convert to dict with dict(iterable)
list_of_tuples = [(2, 2), (3, 3), (4, 4), (5, 5)]
convert_to_dict = dict(list_of_tuples)
print(convert_to_dict)

tuple_of_lists = ([1, 5], [2, 4], [8, 9])
convert_tuple_tolist = dict(tuple_of_lists)
print(convert_tuple_tolist)

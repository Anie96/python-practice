non_empty_dict = {1: ["first", "second"], 2: ["third", "fourth"]}


# to add a new item by key

non_empty_dict[3] = ["i", "am", "third", "value"]
print(non_empty_dict)


# change item by key
non_empty_dict[1] = "My Value has been changed"
print(non_empty_dict)

# update a dictionary

# with dictionary.update()

new_dict = {"one": "First Val", "two": "Second Val"}

non_empty_dict.update(new_dict)
print(non_empty_dict)

# update with **
append_dict = {20: "twenty", 10: "ten"}
second_combine = {**append_dict, **non_empty_dict}
print(second_combine)

# delete item
# with del()
del second_combine[20]
print(second_combine)


# with pop
# dictionary.pop(key)

popped_item = second_combine.pop("two")
print(popped_item)
print(second_combine)


# pop with optional argument
second_popped_item = second_combine.pop("absent", "key not present")
print(second_popped_item)
print(second_combine)

# delete all items
# reassign to empty dictionary
second_combine = {}
print(second_combine)

# with dictionary.clear
print(non_empty_dict)
non_empty_dict.clear()
print(non_empty_dict)

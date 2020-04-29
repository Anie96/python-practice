from copy import deepcopy

mutable_value_dict = {1: ["first", "second"], 2: ["third", "fourth"]}
immutable_value_dict = {"a": "a", "b":"b", "c": "c"}

#assign with =
new_dict = immutable_value_dict
print(new_dict)

#changing an item in one of both will lead to a change in both
immutable_value_dict["a"] ="z"
print(new_dict)
print(immutable_value_dict)

#overcome this with copy
#works only for immutable type values
dict_with_copy = immutable_value_dict.copy()
print(immutable_value_dict)
print(dict_with_copy)


dict_with_copy["a"] = "changed after copy"
print(immutable_value_dict)
print(dict_with_copy)


#for dict with mutable values
mutable_dict_with_copy = mutable_value_dict.copy()
mutable_dict_with_copy[1][0] = "modified"

print(mutable_value_dict)
print(mutable_dict_with_copy)

#overcome this with deepcopy
dict_with_deepcopy = deepcopy(mutable_value_dict)
print(dict_with_deepcopy)

dict_with_deepcopy[1][0] = "modified after deepcopy"
print(mutable_value_dict)
print(dict_with_deepcopy)
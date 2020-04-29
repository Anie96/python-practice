#transverse with for..in

immutable_value_dict = {"a": "a", "b": "b", "c": "c"}

for value in immutable_value_dict.values():
    print(value)


for item in immutable_value_dict.items():
    print(item)
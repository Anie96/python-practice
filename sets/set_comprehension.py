#set comprehension
a_set = {number * 2 for number in range(2, 10) if number % 3 == 1}
print(a_set)


#create immutable set with frozenset()
#works with any iterable

a = frozenset([3,2,1])
print(a)


#you cannot add to a frozenset
# a.add(6)

# print(a)
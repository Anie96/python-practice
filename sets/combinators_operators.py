#check value with in
drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}


#intersection operation
#contains all items that appear in both list, or returns empty set if nothing
for name, contents in drinks.items():
    if contents & {'vodka', 'orange juice'}:
        print(name)


bruss = drinks['black russian']
wruss = drinks['white russian']


#operators
a = {1, 2}
b = {2, 3}


#intersection using & or the set1.intersection(set2)
print(a & b)
print(a.intersection(b))
print(bruss & wruss)

#get union by using | or the set1.union(set2) function
print(a | b)
print(a.union(b))
print(bruss | wruss)

#get difference with '-' or the set1.difference(set2)
print(a - b)
print(a.difference(b))
print(bruss - wruss)
print(wruss - bruss)


#items in one set or orther but noth both uses ^ or set1.symmetric_difference(set2)
print(a ^ b)
print(a.symmetric_difference(b))
print(bruss ^ wruss)

#items in one set or orther but noth both uses <= or set1.issubset(set2)
#a set is a subset of itself
print(a <= b)
print(a.issubset(b))
print(bruss <= wruss)
print(a <= a)


#proper subset use just <
print(a < a)


#items in one set or orther but noth both uses >= or set1.issuperset(set2)
#a set is a subset of itself
print(a >= b)
print(a.issuperset(b))
print(wruss >= bruss)
print(a >= a)

#proper superset with >
print(a > a)

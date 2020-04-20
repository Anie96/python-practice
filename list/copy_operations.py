import copy

#copy list with copy(), list conversion() or [:]
a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]
a[0] = 'integer lists are boring'
print(a)
print(b)
print(c)
print(d)

#assign with equal to
e = [1, 2, 3]

f = e

f[0] = "Tail"

print(e)
print(f)

#copy for list values will be best with mutable types
a = [1, 2, [8, 9]]
b = a.copy()
c = list(a)
d = a[:]
print(a)
print(b)
print(c)
print(d)

a[2][1] = 10
print(b)
print(c)
print(d)

a = [1, 2, [8, 9]]
b = copy.deepcopy(a)
a[2][1] = 10
print(b)
print(a)

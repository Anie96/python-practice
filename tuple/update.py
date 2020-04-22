#you can't modify a tuple but you can concatenate
#you can use id() to check when a variable name is pointing to a new value to confirm modification
t1 = ('Fee', 'Fie', 'Foe')
print(id(t1))
t2 = ('Flop',)
t1 += t2
print(t1)
print(id(t1))

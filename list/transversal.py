#iterate over list with for and in
cheeses = ['brie', 'gjetost', 'havarti']

for cheese in cheeses:
    print(cheese)


#break ends the loop and continue moves to next iteration
cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    if cheese.startswith('g'):
        print("I won't eat anything that starts with 'g'")
        break
    else:
        print(cheese)

#else if the for completed without a break
cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    if cheese.startswith('x'):
        print("I won't eat anything that starts with 'x'")
        break
    else:
        print(cheese)
else:
    print("Didn't find anything that started with 'x'")



#optional else if the for never ran in the first place
cheeses = []
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else:  # no break means no cheese
    print('This is not much of a cheese shop, is it?')

#iterate over multiple sequences with zip
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)


#zip can be used to create iterable types which can be converted into dict, list, tuple
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'

print(zip(english, french))
print(list(zip(english, french)))
print(dict(zip(english, french)))
print(tuple(zip(english, french)))

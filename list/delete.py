marxes = ['Groucho', 'Chico', 'Harpo', 'Peak', 'Anie']

#delete a list item with del keyword by Offset
del marxes[-1]
print(marxes)

#delete an item by value with remove

marxes.remove('Groucho')
print(marxes)

#delete an item with pop method

print(marxes.pop())
print(marxes)

#with index
print(marxes.pop(0))
print(marxes)


#delete with clear method
marxes.clear()
print(marxes)
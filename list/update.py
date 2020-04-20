
marxes = ['Groucho', 'Chico', 'Harpo']

#add item to end of list with append

marxes.append('Another One')
print(marxes)

#add item by offset with insert
marxes.insert(0, 'At Beginning')
print(marxes)

#insert at end
marxes.insert(6, 'At End')
print(marxes)

#duplicate all items with *

duplicate_marxes = marxes * 2
print(duplicate_marxes)

#merge list into another
#using extend()
new_list = ["I Am", "Another List"]
marxes.extend(new_list)
print(marxes)

#using +

another_new_list = ["Another List", "Again"]
marxes += another_new_list
print(marxes)


#Updating a List
#by offset
marxes[2] = "Changed Item"
print(marxes)

#with slice
marxes[4:6] = [1, 2]
print(marxes)

#creating a list via list comprehension

#instead of this

number_list = []
for number in range(1, 10):
    number_list.append(number)

print(number_list)

number_list = list(range(1, 20))
print(number_list)

#you can
number_list = [number for number in range(1, 6)]
print(number_list)


number_list = [number * 2 for number in range(1, 16)]
print(number_list)

multiples_of_two = [number for number in range(1, 20) if number % 2 == 0]
print(multiples_of_two)


#nested comprehension and conditionals
rows = range(1, 6)
cols = range(1, 4)

cells = [(row, col) for row in rows if row% 3 == 0 for col in cols if col % 2==0]
for cell in cells:
    print(cell)

#to unpack
for row, col in cells:
    print(row,col)
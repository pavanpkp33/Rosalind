from itertools import product

# taking inputs from user
array = input("Enter String")
repeat = input("Enter ordering number")

# Strip whitespace
array = array.replace(" ", "")
list = []
for i in array:
    list.append(i)

# get the cartesian product of elements in list
items = product(array, repeat=int(repeat))
# for i in items:
#     print(i)


cartesian_array = []
#sort the items lexicographically
for item in items:
    cartesian_array.append(''.join(item))
cartesian_array.sort()

for i in cartesian_array:
    print(i)

print("Printing every item in a list")

array = [1, 2, 3, 4, 5, 6]
new_array = []

for item in array:
    print("Working on: " + str(item))
    add = item + 14
    print (str(item) + " + 14 = " + str(add))
    new_array.append(add)

print("New array: ", new_array)

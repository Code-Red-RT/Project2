print("Printing every item in a list")

array = [1, 2, 3, 4, 5, 6]
new_array = []

for item in array:
    print("Working on: " + str(item))
    add = item + 14
    print (str(item) + " + 14 = " + str(add))
    new_array.append(add)
for it in array:
incorrect_indent = 20 # added to test change in indentation in part 1 of project

print("New array: ", new_array)

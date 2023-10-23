# Lists are ordered, mutable, allows duplicate elements
from pyrsistent import ny


my_list = ["banana", "cherry", "apple"]
print(my_list)

# Accessing items
item = my_list[0]
print(item)

# Looping through list
for item in my_list:
    print(item)

# Checking if item is in list
if "banana" in my_list:
    print("yes")
else:
    print("no")

# Length of list
len(my_list)

# Adding item to end of list
my_list.append("lemon")

# Adding item at specific index
my_list.insert(1, "blueberry")

# Remove and return last item
my_list.pop()

# Remove item at specific index
my_list.pop(1)

# Clear list
my_list.clear()

# Reverse list
my_list.reverse()

# Sort list
my_list.sort()

# Create list with certain number of elements
my_list = [0] * 5
print(my_list)

# Concatenate lists
my_list2 = [1, 2, 3, 4, 5]
new_list = my_list + my_list2
print(new_list)

# Slicing lists
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = my_list[1:5]  # [2, 3, 4, 5]

# Step in slicing
a = my_list[::2]  # [1, 3, 5, 7, 9] from beginning to end take every second item
a = my_list[::-1]  # [9, 8, 7, 6, 5, 4, 3, 2, 1] reverse list

# Ways to copy a list
list_copy = my_list.copy()
list_copy = list(my_list)
list_copy = my_list[:]

# List comprehension
# [expression for item in list]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
a = [x**2 for x in range(10)]

# [expression for item in list if condition]
# [36, 49, 64, 81]
a = [x**2 for x in range(10) if x > 5]

# [expression if condition else expression for item in list]
# [0, 1, 8, 27, 64, 125, 36, 49, 64, 81]
a = [x**2 if x > 5 else x**3 for x in range(10)]

# [expression for item in list for item2 in list2]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ...]
a = [x**2 for x in range(10) for y in range(10)]

my_list = [0] * 10  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
my_list = "AB" * 10  # "ABABABABABABABABABAB"
print(my_list)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
beginning, *middle, last = numbers
print(beginning)  # 1
print(middle)  # [2, 3, 4, 5, 6, 7, 8, 9]
print(last)  # 10

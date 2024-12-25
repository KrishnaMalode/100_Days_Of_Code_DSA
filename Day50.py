some_list = [int(item) for item in input('Please enter your array: ').split()]
some_list = list(set(some_list))
squared_list = []
for item in some_list:
    squared_list.append(item**2)
print(sum(squared_list))
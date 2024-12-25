some_list = [int(item) for item in input('Please enter your array: ').split()]
for i in range(0,len(some_list)):
    some_list[i] = abs(some_list[i])

some_list = list(set(some_list))
squared_list = []
for item in some_list:
    squared_list.append(item**2)
print(sum(squared_list))

ip = str(input('Enter a string: '))
item_list = []
unique = []
for item in ip:
    item_list.append(item)
    if item not in unique:
        unique.append(item)
for i in range(0,len(unique)):
    print(f'Frequency of {unique[i]} is {item_list.count(unique[i])}')

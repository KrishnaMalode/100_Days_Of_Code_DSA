ip = str(input('Enter a string: '))
item_list = []

for item in ip:
    if item not in item_list:
        item_list.append(item)
    
for item in item_list:
    print(item)




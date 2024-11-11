ip = input('Enter a string to reverse cases: ')

print(ip.swapcase())



list1 = []
for item in ip:
    if item.islower():
        list1.append(item.upper())
    else:
        list1.append(item.lower())
print(''.join(list1))

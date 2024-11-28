list1 = [int(item) for item in input("Enter array elements: ").split()]
list1.sort()
print(f'Smallest Element: {list1[0]} \n Largest Element: {list1[len(list1)-1]}')
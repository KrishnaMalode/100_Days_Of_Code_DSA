list1 = [int(item) for item in input("Enter array elements:").split()]
total_elements = len(list1)
even_count = 0
for item in list1:
    if item%2 == 0:
        even_count +=1

print(f'Even Count: {even_count}\nOdd Count: {total_elements-even_count}')
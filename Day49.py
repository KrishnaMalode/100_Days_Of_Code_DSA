list1 = [int(item) for item in input('Please enter first array: ').split()]
list1 = list1[::-1]
list2 = [int(item) for item in input('Please enter second array: ').split()]

len1 = len(list1)
output = 0
for i in range(0,len1):
    output += list1[i]*list2[i]

print(output)

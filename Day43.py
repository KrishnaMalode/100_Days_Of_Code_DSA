list1 = [int(item) for item in input('Enter array elements: ').split()]
n = len(list1)
count = 0
for item in list1:
    if item%2 == 0:
        count +=1

if  count == n:
    print('Array is even!')
elif count == 0:
    print('Array is odd!')
else:
    print('Array is mixed!')

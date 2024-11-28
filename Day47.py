some_list = [int(item) for item in input('Enter array elements to find largest palindrome: ').split()]
some_list.sort()
max_palindrome = 0
found = False
for item in some_list[::-1]:
    if str(item) == str(item)[::-1]:
        max_palindrome = item
        found = True
        break

if found == False:
    print(f'There is no palindrome in array {some_list}')
else:
    print(f'Max palindrome in the array is: {max_palindrome}')

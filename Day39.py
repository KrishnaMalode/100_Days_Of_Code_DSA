print('Program to check whether 2 strinsg are anagrams or not')
ip1 = str(input("Enter First string: "))
ip2 = str(input("Enter second string: "))
list1 = []
list2 = []
for item in ip1:
    list1.append(item)
for item in ip2:
    list2.append(item)
list1.sort()
list2.sort()

if list1 == list2:
    print(f'{ip1} & {ip2} are anagrams!!')
else:
    print(f'{ip1} & {ip2} are NOT anagrams!!')

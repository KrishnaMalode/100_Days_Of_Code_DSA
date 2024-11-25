ip = str(input("Enter a string: "))
find_this = input('Enter substring to be removed: ')
replace_by =input(f'Enter substring to be replaced by {find_this} => ')
len_found = len(find_this)
index = ip.find(find_this)
ip = ip[:index]+replace_by+ip[index+len_found:]
print(ip)

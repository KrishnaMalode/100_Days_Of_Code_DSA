ip = str(input("Enter a string: "))
find_this = input('Enter substring to be removed: ')
replace_by =input(f'Enter substring to be replaced by {find_this} => ')

if find_this in ip:
    # method1 Replaces first occurence 
    len_found = len(find_this)
    index = ip.find(find_this)
    ip = ip[:index]+replace_by+ip[index+len_found:]
    print(ip)

    ## method2 Replaces first occurence
    ip = ip.replace(find_this,replace_by,1)
    print(ip)
else:
    print("substring not found in string!!")

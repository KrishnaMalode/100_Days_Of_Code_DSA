
ip = str(input('Enter a string with an integer: '))
sum = 0

for item in ip:
    if item.isdigit() :
        sum += int(item)
    

print(sum)
## MEthod 1
ip = int(input("Enter Integer to check no of digits: "))
ip = str(ip)
print(len(ip))

## Method 2
ip = int(input("Enter an Integer to check digits: "))

if(ip == 0):
  print(f'No of digits in integer {ip} are 0')
else:
  count = 0
  temp = ip
  while(temp>10):
    temp = temp/10
    count += 1
count+=1
print(f'No of digits in integer {ip} are {count}')

    

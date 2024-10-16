ip = input("Please Enter Something")

## Method 1
if ip.isalpha() == True :
    print('input is a character')

else:
    print('input is not a character')

## Method 2
if ((ip>='a' and ip<='z') or(ip>='A' and ip<='Z') ):
    print('an alphabet')
else:
    print("not an alpabet")
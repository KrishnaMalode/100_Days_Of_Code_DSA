month = int(input("Enter month number: "))
year = int(input("Enter year number: "))

if (year%4 ==0) or (year%400 ==0):
    if (month == (1,3,5,7,8,10,12)):
        print(f'The {month} of the year {year} has 31 days')
    elif (month == (4,6,9,11)):
        print(f'The {month} of the year {year} has 30 days')
    elif (month ==2):
        print(f'The {month} of the year {year} has 29 days')

else:
    if (month == (1,3,5,7,8,10,12)):
        print(f'The {month} of the year {year} has 31 days')
    elif (month == (4,6,9,11)):
        print(f'The {month} of the year {year} has 30 days')
    elif (month ==2):
        print(f'The {month} of the year {year} has 28 days')

## time and space complexity O(1)
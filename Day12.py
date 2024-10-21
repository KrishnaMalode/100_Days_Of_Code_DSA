
## METHOD 1 : time complexity O(d), Space complexity O(d)
# def sum(num):
#     str_num = str(num)
#     n = len(str_num)
#     num_list = []
#     sum = 0
#     for i in range(0,n):
#         temp = int(str_num[i])
#         num_list.append(temp)

#     for i in range(0,n):
#         sum += num_list[i]
    
#     print(f'Sum of the digits is {sum}')
    
## Method 2 ,time and space complexity, but better code
def sum2(num):
    sum = 0
    for item in str(num):
        sum += int(item)
    print(f'Sum of the degits is: {sum}')


def main():
    try:
        num = int(input("Enter an Integer to add its digits: "))

        if(type(num)!= int):
            raise ValueError('Enter an integer!') 
    except ValueError as e:
        print(f'Invalid Input: {e}')
    
    sum2(num)

if __name__ =="__main__":
    main()
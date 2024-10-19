
def fact(num):
    factorial =1 
    if (num == 0):
        print('Factorial of 0 is 1')
    else:    
        for i in range(1,num+1):
            factorial *= i
    print(f'Factorial of {num} is {factorial}')


def main():
    try:
        ip = int(input("Factorial of the Whole Number to be found: "))

        if (ip<0):
            raise ValueError("Enter a Whole Number")
        print(f'{ip} is a valid input')
    except ValueError as e:
        print(f'Invalid input: {e}')
    
    fact(ip)

if __name__ =="__main__":
    main()

## time complexity = O(n)
## space complexity = O(1)
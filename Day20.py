def is_prime(num):
    
    if num==1:
        print('1 is not a prime number!')
    elif num ==0:
        print(f'0 is neither prime nor composite!')
    elif num==2 :
        print(f'{num} is a prime number!')
    else:
        num_is_prime = True
        for i in range(2,num):
            if num%i==0:
                print(num%i)
                num_is_prime=False
                break
        if num_is_prime == False:
            print(f'{num} is not a prime number!')
        else:
            print(f'{num} is a PRIME number!')

def main():
    try:
        ip = int(input("Enter an number to check if it's a prime number or not: "))
        if type(ip)!=int or ip<0:
            raise ValueError('Please enter a POSITIVE NUMBER!')
    except ValueError as e:
        print(f'INVALID INPUT: {e}')
    is_prime(ip)

if __name__ == "__main__":
    main()
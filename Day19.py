from math import pow

def is_armstrong(num):
    n = len(str(num)) # length of the integer 
    arm_sum = 0
    for item in str(num):
        arm_sum += int(item)**n
    if arm_sum == num:
        print(f'{num} is an Armstrong Number!')
    else:
        print(f'{num} is NOT an armstrong number..')

def main():
    try:
        ip = int(input('Enter an Whole Number To Check For Armstrong: '))
        if type(ip)!=int or ip<0:
            raise ValueError('Please Enter an Whole Number!!!')

    except ValueError as e:
        print(f'Invalid input {e}')
    
    is_armstrong(ip)

if __name__ == "__main__":
    main()



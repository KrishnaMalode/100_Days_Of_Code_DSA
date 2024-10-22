def sum_of_natural_numbers (num):
    sum = 0
    for i in range(1,num+1):
        sum += i
    print(f'Sum of first {num} natural numbers is: {sum}')

def main():
    try:
        num = int(input("Enter natural number to calculate sum: "))
        
        if((type(num)!= int) or (num<1) ):
            raise ValueError("Please enter a natural number")
    except ValueError as e:
        print(f'Invalid Input {e}')
    
    sum_of_natural_numbers(num)

if __name__ =="__main__":
    main()
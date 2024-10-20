def fib(n):
    fib_list = [0,1]
    for i in range(1,n-1):
        num = fib_list[i] + fib_list[i-1]
        fib_list.append(num)
    print(f'fibonacci list: {fib_list}')

def main():
    try:
        n = int(input("Enter number to find out fibonacci series: "))

        if (n<0):
            raise ValueError("Please enter a positive number !")
    except ValueError as e:
        print(f'Invalid input: {e}')
    
    fib(n)

if __name__ == "__main__":
    main()
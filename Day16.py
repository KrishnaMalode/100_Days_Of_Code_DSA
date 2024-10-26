def solution(num):
    factors = []
    for i in range(1,num):
        if (num % i)==0:
            factors.append(i)
    if num ==sum(factors):
        print(f'Entered number: {num} is a Perfect Number!!')
    else:
        print(f'{num} is not a Perfect Number')

def main():
    try:
        ip = int(input('Enter a positive number: '))
        if((type(ip)!= int) or (ip<1)):
            raise ValueError('PLEASE ENTER A POSITIVE NUMBER!!!!')
    except ValueError as e:
        print(f'INVALID INPUT {e}')
    solution(ip)

if __name__ == "__main__":
    main()
        
def is_palindrome(num):
    num_list = []
    for item in str(num):
        num_list.append(item)
    if num_list==num_list[::-1]:
        print(f'{num} is a Palindrome Number!!')
    else:
        print(f'{num} is NOT a Palindrome Number :(')
    
def main():
    try:
        ip = int(input('PLEASE ENTER A POSITIVE INTEGER: '))
        if ip<0 or type(ip)!=int:
            raise ValueError('PLEASE ENTER A NUMBER GREATER THAN ZERO!!!!!!')
    except ValueError as e:
        print(f'INVALID INPUT {e}')
    is_palindrome(ip)

if __name__ =="__main__":
    main()
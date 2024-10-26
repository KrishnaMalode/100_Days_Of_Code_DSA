## to check whether a number is a strong number or not

def fact(num):
    factorial = 1
    for i in range(1,num+1):
        factorial *= i
    return factorial

def strong_num(num):
    sum_of_fact = 0
    str_num = str(num)
    list = []
    for item in str_num:
        list.append(int(item))
    for item in list:
        sum_of_fact += fact(item)
    if sum_of_fact == num:
        print(f'Entered Number is a String Number!!')
    else:
        print(f'Not a Strong Number')

def main():
    try:
        ip = int(input('Enter to check if num is a strong num: '))
        if(type(ip)!=int or ip<1):
            raise ValueError('PLEASE ENTER AN POSITIVE INTEGER')
    except ValueError as e:
        print(f'Invalid Input!!')
    
    strong_num(ip)

if __name__ == "__main__":
    main()
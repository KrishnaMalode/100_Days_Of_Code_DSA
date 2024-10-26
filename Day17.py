import math as m

def factors(num):
    factors_list = []
    
    if (num == 0):
        print('Number entered is 0 and has no Factors!!')
    elif (num<0):
    
        i = num
        num = num*(-1)   # to make the number positive 
        for k in range(i,(abs(int(m.sqrt(num))))+1):
            factors_list.append(k)
            factors_list.append(num//k)
        print(f'Factors of {num} are: {sorted(set(factors_list))}')
    else:       
    
        for i in range(1,(abs(int(m.sqrt(num))))+1):
            if (num % i ==0):
                factors_list.append(i)
                factors_list.append(num // i)
        print(f'Factors of {num} are: {sorted(set(factors_list))}')

def main():
    try:
        ip = int(input('Please enter an integer to get factors: '))
        if(type(ip)!=int):
            raise ValueError('PLease enter an integer!!')
    except ValueError as e:
        print(f"Invalid Input: {e}")
    factors(ip)

if __name__ == "__main__":
    main()
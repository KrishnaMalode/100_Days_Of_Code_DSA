import sympy 

def sum_of_prime_numbers(num):
        executed = False
        prime_no_list = list(sympy.primerange(0,num))
        for i in range(0,len(prime_no_list)):
            rem = sympy.isprime(num - prime_no_list[i])
            if rem == True:
                rem = num -prime_no_list[i]
                print(f'{num} is a combination of prime numbers {prime_no_list[i]} and {rem}')
                executed = True
                break
        if executed == False:
            print('Odd numbers cannot be written as the sum of two odd primes because the sum of two odd numbers is always even')
    
        

    

def main():
    ip = int(input("Enter a Positive Number: "))
    sum_of_prime_numbers(ip)

if __name__ =="__main__":
    main()
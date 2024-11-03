def pyramid(num):
    list_of_odds = []
    # code to generate list of odd numbers of length that is equal to number inputted
    for i in range(1,2*num):
        if i%2==1:
            list_of_odds.append(i)
    # code to print the actual pyramid
    for item in list_of_odds:
        print('*'*item,'\n')

def main():
    try:
        ip = int(input('Enter Positive Number to generate a pyramid: '))
    except ValueError as e:
        print(f'INVALID INPUT {e}')
    pyramid(ip)

if __name__ =="__main__":
    main()

        

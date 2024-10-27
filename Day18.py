def add_fractions(x1,y1,x2,y2):
    #x = numerator & y = denominator
    print(f'sum of the two fractions is: {(x1*y2 + x2*y1)}/{y1*y2}')

def main():
    try:
        x1= int(input('Enter numerator of first fraction: '))
        y1= int(input('Enter denominator of first fraction: '))
        x2= int(input('Enter numerator of second fraction: '))
        y2= int(input('Enter denominator of second fraction: '))

        if(type(x1)!=int or type(x2)!=int or type(y1)!=int or type(y2)!=int):
            raise ValueError('Please enter an integer: ')
    except ValueError as e:
        print(f'INVALID INPUT!! ={e}')
    add_fractions(x1,y1,x2,y2)


if __name__ == "__main__":
    main()
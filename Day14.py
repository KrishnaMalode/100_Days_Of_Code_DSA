def reverse_num(num):
    str_num = str(num)
    list = []
    for item in str_num[::-1]:
        list.append(item)

    
    print(f'Reversed number is: {"".join(list)}')

def main():
    try:
        num = int(input("Please an intger to be REVERSED: "))

        if(type(num)!=int):
            raise ValueError("Please Enter an Integer !")
    except ValueError as e:
        print(f'Invalid Input! == {e}')

    reverse_num(num)

if __name__ =="__main__":
    main()
def zeroes_to_one(num):
    num_list = []
    for item in str(num):
        if item == '0':
            num_list.append('1')
        else:
            num_list.append(item)
    
    print(''.join(num_list))
    

def main():
    try:
        ip = int(input('Enter a number: '))
    except ValueError as e:
        print(f'INVALID INPUT {e}')
           
    zeroes_to_one(ip)

if __name__ =="__main__":
    main()   
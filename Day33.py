ip = str(input('Enter a string to check for palindrome: '))

if  ip == ip[::-1]:
    print(f'{ip} is a palindrome string!')
else:
    print(f'{ip} is not palindrome')
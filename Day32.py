ip = str(input("Enter a string: "))

vowels = ['a','e','i','o','u','A','E','I','O','U']
word = []
for item in ip:
    if item in vowels:
        pass
    else:
        word.append(item)
print(''.join(word))
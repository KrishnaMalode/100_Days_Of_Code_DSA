import fnmatch

wildcard = input('Enter wildcard word: ')
normal = input('Enter the normal word: ')

if fnmatch.fnmatch(normal,wildcard):
    print('Yes they match!!')
else:
    print('They do not match :(')


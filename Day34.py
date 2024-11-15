ip = str(input('Enter an algbraic expression to remove brackets: '))

alg_list = []

for item in ip:
    if item =='(' or item ==')':
        alg_list.append('')
    else:
        alg_list.append(item)

print(''.join(alg_list))
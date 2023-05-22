number = int(input('Input number  '))
if number < 0 or number > 100000:
    print('This number is not liquid')
divider = 2
while number > divider:
    if number // divider != 0:
        divider += 1
        continue
    else:
        print(f'{number} is a not ordinary')
        break
else:
    print(f'{number} is an ordinary')



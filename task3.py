from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
check = 10
checkout = 1
while checkout <= check:
    checkout += 1
    number = int(input('Input nuber from 0 to 1000'))
    if number > num:
        print("more")
        continue
    if num > number:
        print('less')
        continue
    if num == number:
        print('You are lucky')
    break
print(f'You are  not lucky {num}')




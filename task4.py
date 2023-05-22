number = input('input a number')
if number.isdigit():
    hex(int(number))
    oct(int(number))
else:
    ascii(number)

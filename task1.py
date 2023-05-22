a = int(input('Input first long'))
b = int(input('Input second long'))
c = int(input('Input third long'))
if (b+c) < a or (a + c) < b or (a + b) < c:
    print('You input wrong value')
if c == b == a:
    print('These triangle is equilateral')
if a==b or b == c or a == c :
    print(' This triangle is isosceles')
else:
    print(' This is an usual triangle')

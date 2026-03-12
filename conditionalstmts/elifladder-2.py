sub1 = int(input('Enter sub 1 Marks : '))
sub2 = int(input('Enter sub 2 Marks : '))
sub3 = int(input('Enter sub 3 Marks : '))
avg = (sub1+sub3+sub3)/3
if sub1<35 or sub2<35 or sub3<35:
    print('Result is Failed ')
elif avg>=91:
    print('Result is Outstanding')
elif avg>=81:
    print('Result is A Grade')
elif avg>=71:
    print('Result is B Grade')
else:
    print('Result is C Grade')
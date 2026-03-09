sub1 = int(input('Enter subject 1 marks : ')) #30
sub2 = int(input('Enter subject 2 marks : ')) #60
sub3 = int(input('Enter subject 3 marks : ')) #70
#   30>34-F     60>34-T    70>34-T
if sub1>34 and sub2>34 and sub3>34:
    print('You got passed  in the exam')
    print('You are Promted to the Second Year')
else:
    print('You got Failed in the exam')
    print('Get ready for the supply exams')

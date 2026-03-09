sub1 = int(input('Enter subject 1 Marks : '))  # 32
sub2 = int(input('Enter subject 2 Marks : '))  # 50
sub3 = int(input('Enter subject 3 Marks : '))  # 60

                                           # F       T          T
if sub1>34 and sub2>34 and sub3>34:       #32>34 and 50>34 and 60>34
    print('Student got passed in the exams')
                                      # T        F         F
if sub1<35 or sub2<35 or sub3<35:     #32<35 or 50<35  or 60<35
    print('Student got failed in the exams')

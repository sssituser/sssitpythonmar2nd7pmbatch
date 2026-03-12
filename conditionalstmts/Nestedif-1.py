'''
Write a program to check the given number is +ve and single digit
'''
num = int(input('Enter a number : '))  # num = -100
if num>0:  # -100>0 -F
    if num<10: # 1000<10-F
        print(f'{num} is +ve and single digit')
    else:
        print(f'{num} is +ve but not a single digit')
else:
    print(f'{num} is not a +ve number')
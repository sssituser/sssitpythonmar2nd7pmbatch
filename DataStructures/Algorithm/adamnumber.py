'''
Write a program to check given number is Adam or not.
isadam(num)

What is Adam number ?
num = 12
numsq = 144


rev num = 21
revnumsq = 441
rev=144
        Algorithm :
        1.Read num   = 12
        2.Find the sqare of number =144
        3.Reverse number = 21
        4.Reversenumber squre = 441
        5.Reverse the reversenumbersqaure = 144
        6.compare square of two number 144 == 144 =>True
'''
def square(num):
    return num*num

def reverse(num):
    num = str(num)
    return int(num[::-1])

def isadam(num):
    return square(num)   == reverse(square(reverse(num)))


print(isadam(12))
print(isadam(10))
print(isadam(6))
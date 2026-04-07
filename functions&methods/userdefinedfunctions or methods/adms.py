'''
Write a program to generate list of adam numbers for the given range
start = 10 end = 100
num = 12        rev = 21
numsq = 144   revsql = 441 reverse= 144
'''
def square(num:int):
    return num*num
def reverse(num:int):
    rev = 0
    while num>0:
        rev = rev*10+num%10
        num = num//10
    return rev    
def isadam(num):
    return square(num)== reverse(square(reverse(num)))

def getadams(start:int,end:int):
    res = ''
    for num in range(start,end+1):
        if isadam(num):
            res = res + str(num)+","
    return res[0:len(res)-1]+"."

print(getadams(1,100))
    
'''
Write a program to find the sum of the n numbers for the given number
num = 5    sum = 1+2+3+4+5=>15

'''
def sum(num):
    if num==1:
        return 1
    else:
        return num+sum(num-1)
    
print(sum(10))
'''
sum(5)=>return 5+10
'''





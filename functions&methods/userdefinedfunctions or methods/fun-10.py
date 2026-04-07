'''
    Write a program to generate a febonacci series for the given number
    num = 1  0
    num = 2 0 1
    num = 3 0 1 1
    num = 4 0 1 1 2
    num = 5 0 1 1 2 3
    num = 6 0 1 1 2 3 5
'''
def genfebobnaci(num:int): #num = 3
    if num == 1:
        return 0
    if num == 2:
        return 1
    num1 = 0
    num2 = 1
    for i in range(1,num-1):
        result = num1+num2 # i = 1 rs  = 1 num1 = 1 num2 = 1  i = 2 rs = 2 num1 = 1 num2 = 2 i =  3
        num1 = num2
        num2 = result
       
    return result   
print(genfebobnaci(5))
print(genfebobnaci(6))
print(genfebobnaci(7))
     
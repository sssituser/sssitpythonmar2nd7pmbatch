'''
write a program to find the factorial of a given number
num = 4   4! = 1*2*3*4=>24
num = 5   5! => 120

'''

def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
    
print(factorial(5))
print(factorial(4))
#factoirial(5)=> return 5*fact(4)=>4*fact(3)=>3*fact(2)=>2*fact(1)

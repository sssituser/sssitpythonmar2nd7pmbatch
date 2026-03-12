'''
    Write a program to display the stmt n times
    stmt = "Welcome to Online Training for Python"  num = 8
    num = 3
        1.Welcome to Online Training for Python
        2.Welcome to Online Training for Python
        3..Welcome to Online Training for Python
    num = 5
         1.Welcome to Online Training for Python
         2.Welcome to Online Training for Python
         3.Welcome to Online Training for Python
         4.Welcome to Online Training for Python
         5.Welcome to Online Training for Python
        
'''
num = int(input('Enter a number : '))
start = 1
end = num
while start <= end: 
    print(f'{start}. Welcome to Online Training for Python') 
    start = start+1 
'''
num = 10    2 4 6 8 10 12 14 16 18 20
num = 10    3 6 9 12 15 18 21 24  27 30

write a program to generate number from given number to 1
num = 5   result 5 4 3 2 1
num = 10        10 9 8 7 6 5 4 3 2 1
-----------------------------
num = 10  10 8 6 4 2 0
num = 20  20 17 14 11 8 5 2 

'''
num = int(input('Enter a number : '))
start = num
end = 1
while start >=  end:
    print(start,end=" ")
    start = start-1
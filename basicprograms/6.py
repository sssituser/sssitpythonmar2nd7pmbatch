'''
    Write a program to read integer,float,boolean and complex  data and
    display them
'''
# Reading the Data
print("======Reading the Data=======")
s = input("Enter a string : ")
num =int(input('Enter a number : '))
f = float(input('Enter a float value : '))
b = bool(input('Enter boolean value : '))
c = complex(input('Enter a complex number : ')) 

#Displaying the Data
print("=======Displaying the Data=========")
print(f's = {s} and its type is {type(s)}')
print(f'num = {num} and its type is {type(num)}')
print(f'f = {f} and its type is {type(f)}')
print(f'b = {b} and its type is {type(b)}')
print(f'c = {c} and its type is {type(c)}')
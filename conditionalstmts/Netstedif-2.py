'''
Write a program to check the fever condition of a Patient
'''
temp  = int(input('Enter Temp : '))
if temp>97:
    if(temp<=100):
        print(f'{temp} Patient has a fever')
    else:
        print(f'{temp} Patient has a high fever')
else:
    print(f'{temp} is a normal temprature')
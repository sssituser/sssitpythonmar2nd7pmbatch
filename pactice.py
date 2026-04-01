num = int(input('Enter a number to check prime or not : '))
fcount = 0
for i in range(1,num+1):# i = 1 i = 2 i = 3 i = 4 i = 5
    if num%i == 0:
        fcount=fcount+1 #fcount = 2
if fcount == 2:
    print(f'{num} is a prime')
else:
    print(f'{num} is not a prime')
        
        
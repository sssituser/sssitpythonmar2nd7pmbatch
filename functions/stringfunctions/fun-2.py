s ="arunkumar"
#1. Directly dealing with the chcaracter.
for char in s:
    print(char)
    
#2. for loop using +ve idexing

for i in range(0,len(s)):
    print(f'{i}--->{s[i]}')
    
#2. for loop using +ve idexing

len = len(s)

for i in range(-len,0,1):
    print(f'{i}--->{s[i]}')
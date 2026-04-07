'''
Write  a program to generate the list of palindromes for the given range.
Example :
start = 10
end = 90
output : 11,22,33,44,55,66,77,88.
functionname : getpalindromes
parameters  : two parameters
result :string
'''

def ispalindrome(num:int): #num = 11
    res = str(num) # res = '11
    return res == res[::-1] # '11' == '11'

def getpalindromes(start:int,end:int): #start = 10  end = 90
    res=''
    for i in range(start,end+1):
        if ispalindrome(i):
            res = res+str(i)+","
    return res[0:len(res)-1]+"."
        
print(getpalindromes(10,90))
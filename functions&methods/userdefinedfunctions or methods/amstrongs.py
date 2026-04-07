
'''
Write a program to generate list of Armstrongs for the given range.
start = 1
end = 1000
ouput :1,2,3,4,5,6,7,8,9,153,370,371,407.

num = 153    1cube+5cube+3cube = 153
num = 1634   1pow4+6pow4+3pow4+4pow4 = 1634
function name : getamrstrongs
paramters : two pramters
reuslt :string
'''

def isarmstrong(num:int): # num = 153 
    copy = num # copy = 153
    pow = len(str(num)) # pow = 3
    sum = 0
    while num>0: # num = 153 num = 15>0-T num =1>0-T 0>0-F
        digit = num%10 #digit = 153%10 digit = 3 digit = 15%10 digit = 5 digit = 1%10 digit = 1
        sum = sum + digit**pow # sum = 27 sum = 152 sum = 153
        num = num//10 # num = 153//10 num = 15//10 num = 1 //10 num = 0
    return copy == sum   
def getarmstrongs(start:int,end:int):
    res = ''
    for i in range(start,end+1):
        if isarmstrong(i):
            res = res+str(i)+","
    return res[0:len(res)-1]+"."

print(getarmstrongs(1,1000))
'''
    Write Program to check given number is Armstrong :
    num = 153   1cube+5cube+3cube => 153
    num = 1634  1pow4+6pow4+3pow+4pow4=> 1634
    steps :
    1.speparate the digits and    count
    2.spearate th digits find power of digits 
    3.find the sum of the power of the digits
    4.compare orginual number with sum
'''
def isarmstrong(num:int): # 153
    count = 0
    copy = num
    while num>0:
        count=count+1
        digit = num%10
        num=num//10
    num = copy
    sum = 0
    while num>0: # num = 153>0 -T 15>0-T 1>0-T 0>0-F
        digit =num%10 # digit = 3 digit = 5 digit = 1
        sum = sum + digit ** count # sum = 3**3 ;27  27+5**3; sum = 152 sum = 153
        num =num//10 # num = 153//10 num = 15//10 num = 1//10 num = 0
    return sum == copy
    
print(isarmstrong(153))
print(isarmstrong(123))
print(isarmstrong(1634))


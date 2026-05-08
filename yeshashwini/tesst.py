'''
Write a program to find the lucky number for the given date of birth
dob ="19-Jan-2000"
:
Lucky number : 
date = 19
mon = 1
year = 2000
sum = 19+1+2000 => sum = 2020 => 2+0+1+9 => 12=>1+2=>3
'''
def monthtexttonum(month): #Febrauary
    month = month.lower()
    months = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
    for i in range(len(months)):
        if  month.__contains__(months[i]):
            return i+1
    return 0
def digitsum(num):
    sum = 0
    while num>0:
        digit = num%10
        sum = sum + digit
        num = num//10
    return sum
def getluckunuber(dob):
    li = dob.split("-") # ["19","jan","2000"]
    date  = int(li[0])
    month  = monthtexttonum(li[1])
    year  = int(li[2])
    sum = date+month+year # 2020
    while sum>9:
        sum = digitsum(sum)
    return sum

print(getluckunuber("11-April-2004")) # 2019=>3
    
    

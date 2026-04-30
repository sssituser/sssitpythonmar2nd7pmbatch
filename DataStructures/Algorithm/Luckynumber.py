'''
Write a program which reads date of birth , and return a single digit in
bet 0 to 10   and the num can be treated luckynumber.
note : Dob = '19-jan-2000'
date is a number
month - is always text min 3 characters 
year number
Dob = '19-jan-2000'
date = 19
month = jan (1)
year = 2000
19+1+2000=>2020 -> 2+0+2+0 => 4 is the lucky number
2019=>2+0+1+9=>12>9=> 1+2 => 3 is the lucky number
Alogrithm :(Steps)
1.dob = '19-Jan-2000' getluckynumber(dob)
2.split date of birth given below 
3.convert them into numbers
date = 19
month = convertmonthtexttonum('jan') month = 1
year = 2000
4.find the sum of the date+month+year
5.sum is>9
6.find sum of the digits of number(sum is greaterthan>9 repeat)
7.send lucky number

dob = '19-Jan-2000':
convertmonthtexttonum(li[1])# month
1.list of months
2.compare month with list months 
3.if becomes equal any moth at store index of the month with +1
4.reurn the number

'''

def convertmonthtexttonum(month): # month = "March"
    month = month.lower()
    months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    for i in range(0,len(months)):
        if month.__contains__(months[i]):
            return i+1
    return 0
def digitsum(num):
    sum = 0
    while num>0:
        sum = sum+num%10
        num//=10
    return sum

def getluckynumber(dob):
    li = dob.split('-')
    date = int(li[0])
    month = convertmonthtexttonum(li[1])
    year = int(li[2])
    sum = date+month+year
    while sum>9:
        sum = digitsum(sum)
    return sum
dob = '19-Jan-2000'
print(getluckynumber(dob))
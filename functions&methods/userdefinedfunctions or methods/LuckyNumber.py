'''
Write a program to find the lucky number of a given Date of birth.
input = "12-Oct-1998 12+10+1998 2020 => 2+0+2+0=> 4 Lucky Numbers is 4
         12-Nov-2011   23+11+2011 => 23+2022 => 2045 =>2+0+4+5=>11=>1+1 => Lucky Number is 2
         24-Sept-2014 
Date of Birth Rules:
1.Format must be DD-MM-YEAR
2.MM is always in a string , string must be min chars 3 or more.
Steps :
   1. "12-Oct-1998"
   2. Separate Date Month Yeare
   3. "12"    Oct   1998
    convert above date of birth into numbers and add them
   4. 12    10    1998
   5 .12+10+1998 =>>2020 > 9 2+0+2+0=>4>9
   6.reuturn number

'''
def convertmonthtextostring(month:str):# jan
    months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    month = month.lower()
    for i in range(0,len(months)):# i = 0
        if month.__contains__(months[i]):
            return i+1
def digitsum(num:int): # 123
    sum = 0
    while num>0: 
        digit = num%10 
        sum = sum + digit 
        num = num//10 
    return sum
def getluckynuber(dob:str):
    result = dob.split("-")
    date  =  int(result[0])
    month =  convertmonthtextostring(result[1])
    year = int(result[2])
    sum = date+month+year
    while(sum>9):
        sum = digitsum(sum)
    return sum

dob = input("Enter DOB : ")
print(f"Your Lucky Number : {getluckynuber(dob)}")
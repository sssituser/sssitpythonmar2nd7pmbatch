'''
Write a program to find the max number from the given list
li = [100,102,301,412,325,789,567]
Examle :
    1,2,3,4,5,9,7
    Maxnumber : 9754321
    
    
   from the given [100,102,301,412,325,789,567]
    maxdigit list =[1,2,3,4,5,9,7]
    sortlist in desc =[9,7,5,4,3,2,1]
    listtonum = 9754321
    
    
Steps:
1.li = [100,102,301,412,325,789,567]
2.From the list we get each number and find the maxdigit of that number and store list
3.Maxdigitlist
4.sort the list in desc
5.convert list into a number

'''
def getmaxdigit(num:int):
    max = num%10
    while num>0:
        digit = num%10
        if digit>max:
            max = digit
        num = num//10
    return max
def getmaxdigitlist(li:list):
    maxdigitlist=[]
    for num in li:
        maxdigitlist.append(getmaxdigit(num))
    return maxdigitlist

    
def sortlistindesc(li:list):
    li.sort()
    li.reverse()
    return li
    
def listtonum(li:list): #[4,5,6]
    res = 0
    for num in li: #
        res = res*10+num #456
    return res

def getmaxnumber(li:list):
    return  listtonum(sortlistindesc(getmaxdigitlist(li)))

li = [100,102,301,412,325,789,567]

print(f'max numer is : {getmaxnumber(li)}')
# print(listtonum([4,5,6]))
# print(getmaxdigit(456))
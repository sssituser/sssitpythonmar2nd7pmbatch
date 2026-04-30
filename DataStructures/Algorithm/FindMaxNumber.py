'''
Li  = [123,110,345,678,569] from the given list find the max numbers
as 3,1,5,8,9 using max digit form a max number 98531.

Steps:
1.given li = [123,110,345,678,569] # getmaxnumber(list)
2.GetMaxgit from each number # getmaxdigit(num) =>3
                                                getmaxdigitlist(lisst)
3.find the max digit from all the numbersj present in the list maxdigitlist [3,1,5,8,9]
4.sort maxdigitlist into desc [9,8,5,3,1]# sortlistdesc(li)
5.convret list to number 98531 # listtonum(li)


'''

def getmaxdigit(num): # 321
    max = num%10 # max = 1
    while num>0: # 321>0-T 32>0-T 3>0-T 0>0-F
        digit = num%10 # digit = 321%10 digit = 1 digit = 32%10 digit = 2 digit = 3%10 digit = 3
        if digit>max:
            max = digit # max = 2 max = 3
        num=num//10 # num = 321//10 num = 32//10 num = 3//10 num = 0
    return max
def getmaxdigitlist(li):
    maxdigitlist = []
    for num in li:
        maxdigitlist.append(getmaxdigit(num))
    return maxdigitlist
def sortlistdesc(li):
    li.sort()
    li.reverse()
    return li
def listtonum(li):
    res = 0
    for num in li:
        res = res*10+num
    return res
     
def getmaxnumber(li):
   return listtonum(sortlistdesc(getmaxdigitlist(li)))

li = [123,110,345,678,569]
print(getmaxnumber(li))
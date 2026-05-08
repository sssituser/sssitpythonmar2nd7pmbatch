li = [123,456,789]
# [3,6,9] => [9,6,3]=> 963

def sortlidesc(li):
    sorted(li)
    li.reverse()
    return li
def getmaxdigit(num):
    max = num%10
    while num>0:
        digit = num%10
        if digit>max:
            max = digit
        num = num//10
    return max

def getmaxdigits(li):
    mxdigili =[]
    for i in li:
        mxdigili.append(getmaxdigit(i))
    return mxdigili


def litonum(li):# [9,6,3]
    res =0
    for i in li:
        res = res*10+i
    return res
        


def getmaxnumber(li):
    return litonum(sortlidesc(getmaxdigits(li)))

print(getmaxnumber(li))
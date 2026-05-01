
def bubble_sort(li):
    n =len(li)
    for i in range(n):
        for j in range(0,n-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
li = [5,8,1,4,7]
print(li)
bubble_sort(li)
print("After sorting-------")
print(li)
                
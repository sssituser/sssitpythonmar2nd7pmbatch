li = [10,20,30,40,45,50,52,67,88,99]
key = int(input('Enter Element to be searched : '))
low = 0
high = len(li)-1

while low<=high:
    mid = (low+high)//2
    if li[mid] == key:
        print(f'Element found at :{mid} location')
        break
    elif key<li[mid]:
        high=mid-1
    else:
        low = mid+1
print(f'{key} Not Found')

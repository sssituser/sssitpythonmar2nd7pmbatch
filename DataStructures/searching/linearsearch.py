nums = [56,67,89,23,12,1,3,15,53,12,13,14,51,76,75,7,4]

search = int(input('Enter a number to Search : '))
count = 0
for i in range(1,len(nums)):
    if search == nums[i]:
        print(f'{search} found  at : {i} location')
        count = count+1
if count == 0:
    print(f'{search} element is not found')
    
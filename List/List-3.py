li = [23,45,67,89,90]
print('Displaying the elements of the list using for loop')
for item in li:
    print(item,end="  ")
    
print('\nDisplaying the elments using +ve indexng ')
for index in range(0,len(li)):
    print(f'index  = {index} = >{li[index]}')
    
print(f"Total elements : {len(li)}")

print("\nDisplaying the element using -ve index")
for index in range(-5,0):
    print(f'index = > {index} => {li[index]}')
    
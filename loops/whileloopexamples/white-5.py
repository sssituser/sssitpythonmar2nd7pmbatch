'''
Write program to find the factorial of a given number
num = 5   num! = 5*4*3*2*1 = 1*2*3*4*5 => 120
num = 4   4! = 1*2*3*4 =>24
'''
num = int(input('Enter a number  : '))
start = 1
end = num
fact = 1            
      
while start <= end:  #1<=4-T 2<=4 3<=4 4<=4-T 5<=4-F
    fact = fact*start # fact = 1 fact = 2 fact = 6 fact = 24
    start = start+1 # 
print(fact)
    



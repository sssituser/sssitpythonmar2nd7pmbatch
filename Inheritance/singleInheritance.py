class Calculator:
    def __init__(self,a,b):
       self.a = a
       self.b = b
    def sum(self):
        print(f'Sum is {self.a+self.b}')     
    def sub(self):
        print(f'Sub is {self.a-self.b}')      
    def mul(self):
        print(f'Mul is {self.a*self.b}')     
    def div(self):
        print(f'Div is {self.a/self.b}')       
import math
class SciCalcy(Calculator):
    def __init__(self,a,b):
       super().__init__(a,b) #  sending the data from child class constructor to Parent class constructor
    def sine(self,val):
        print(f'Sine {val}  {math.sin(val)}')
    def cons(self,val):
        print(f'Cons {val}  {math.cos(val)}')
s1 = SciCalcy(5,2)
s1.sum()
s1.sub()
s1.mul()
s1.div()
s1.sine(90)
s1.cons(0)    
    

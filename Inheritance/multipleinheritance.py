class A:
    def readnums(self):
        self.a = int(input('Enter a number : '))
        self.b = int(input('Enter a nuber : '))
        
    def shownums(self):
        print(f'a = {self.a}\nb = {self.b}')
class B:
    def add(self):
        print(f'sum is : {self.a+self.b}')

class C:
    def sub(self):
        print(f'sub is :{self.a-self.b}') 
class D(A,B,C):
    def mul(self):
        print(f'mul is : {self.a*self.b}')
        
        
p = D() 
p.readnums()
p.shownums()
p.sub()
p.add()
p.mul()         
    
        
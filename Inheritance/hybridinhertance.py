class A:
    def readnums(self):
        self.a =int(input('Enter  num1 : '))
        self.b =int(input('Enter  num2 : '))
    def shownums(self):
        print(f'a = {self.a}\t b = {self.b}')
    
class B(A):
    def sum(self):
        print(f'sum is :{self.a+self.b}')
    
class C:
    def mul(self):
        print(f'mul is :{self.a*self.b}')
    
class D(B,C):
    def div(self):
        print(f'quo is : {self.a//self.b}')
        
p = D()
   
p.readnums()
p.shownums()
p.sum()
p.mul()
p.div()

class A:
    def readnums(self):
        self.a = int(input('Enter a number : '))
        self.b = int(input('Enter b number : '))
        
    def shownums(self):
        print(f'a = {self.a}\tb = {self.b}')
        
        
class B(A):
    def sum(self):
        print(f'sum is :{self.a+self.b}')       
class C(A):
    def mul(self):
        print(f'Mul  is :{self.a*self.b}') 
class D(A):
    def div(self):
        print(f'Quo is :{self.a%self.b}')
        
r =B()
r.readnums()
r.shownums()
r.sum()

c = C()
c.readnums()
c.shownums()
c.mul()

d = D()
d.readnums()
d.shownums()
d.div()




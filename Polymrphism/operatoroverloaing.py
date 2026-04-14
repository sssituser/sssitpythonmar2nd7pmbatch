class Test:
    def readab(self):
        self.a = int(input('Enter value of a : '))
        self.b = int(input('Enter value of b : '))
    def showab(self):
        print(f'a = {self.a}\tb = {self.b}')
    def __add__(self, other): # self will copy the values t1 object and other can copy t2 object values
        r = Test()
        r.a = self.a+other.a
        r.b = self.b+other.b
        return r
print("================Objct - 1  Information======================")

t1 = Test()
t1.readab()
t1.showab()

print("================Objct - 2  Information======================")

t2 = Test()
t2.readab()
t2.showab()

print("================Objct - 3  Information======================")

t3 = Test()
t3= t1+t2
t3.showab()
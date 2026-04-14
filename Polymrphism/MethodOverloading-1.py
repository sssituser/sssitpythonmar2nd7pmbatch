class Test:
    def show(self,str):
        print(str)
    def area(self,l=0,b=0,r=0.0):
        if(l!=0 and b==0 and r ==0.0):
            print(f'Area of a square is :{l*l} ms')
        if(l!=0 and b!=0 and r==0.0):
            print(f'Area of a Rectagle is : {l*b} ms')
        if( r!=0.0):
            print(f'Area of a circle : {3.14*r*r}')
            
# non static method can be accessed using object
t = Test()
t.show(12)
t.show('hi')
t.show(678.78)
t.area(4)
t.area(4,5)
t.area(r = 5.6)
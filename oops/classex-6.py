class Product:
    def __init__(self):
        self.pid = 111
        self.pname  ="TestProduct"
        self.pprice = 90000
        print("Hi Iam Default Constructor")
        
    # def __init__(self, pid,pname,pprice):
    #     self.pid = pid
    #     self.pname = pname
    #     self.pprice = pprice
    #     print("Hi Iam Parameterised Constructor")
        
    def getproduct(self):
        print(f'Product ID : {self.pid}')
        print(f'Product Name : {self.pname}')
        print(f'Product Price : {self.pprice}')
p1 = Product()
p1.getproduct()

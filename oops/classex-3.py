class Product:
    def setproduct(self,pid,pname,pprice): ## local variables
        self.prodid = pid
        self.prodname = pname
        self.prodprice = pprice
        
    def getproduct(self):
        print(f'Product id : {self.prodid}')
        print(f'Product name : {self.prodname}')
        print(f'Product Price : {self.prodprice}')
        
print("===========Prod-1 Object===========")
prod1 = Product()
prod1.setproduct(111,"Soap",50)
prod1.getproduct()        

print("===========Prod-2 Object===========")
prod2 = Product()
prod2.setproduct(112,"AC",50000)
prod2.getproduct()        
    
print("===========Prod-3 Object===========")
prod3 = Product()
prod3.setproduct(113,"Washing Machin",55000)
prod3.getproduct()        

print("===========All Products===========")
prod1.getproduct()
prod2.getproduct()
prod3.getproduct()        
    
    
    
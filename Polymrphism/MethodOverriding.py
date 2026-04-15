class Chicken:
    def getprice(self):
        print('Chicken Price : Rs.300')
    def show(self):
        print("Hi Iam show method from chicken")
        
class Restuarant(Chicken):
    def getprice(self):
        print('Chicke 65 Price : Rs.500')
r = Restuarant()
r.show()
r.getprice()
r = Chicken()
r.getprice()
        

        
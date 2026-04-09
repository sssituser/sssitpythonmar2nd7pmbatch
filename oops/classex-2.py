class Employee:
    def setemployee(self,eid,ename,esal): # eid,ename,esal local variables
        self.id = eid # self.id instance variables or non static members
        self.name = ename
        self.sal = esal
       
        #self.id self.name self.sal  are non static members, can be accessed anywhere in the class
    def getemployee(self):
        print(f'Employe ID: {self.id}')
        print(f'Employee Name : {self.name}')
        print(f'Employee Salary : {self.sal}')
        
print("========Employee 1 object============")
emp1 = Employee()
emp1.setemployee(111,'abc',60000)
emp1.getemployee()
print("========Employee 2 object============")
emp2 = Employee()
emp2.setemployee(112,"par",70000)
emp2.getemployee()
print("========Employee 3 object============")
emp3 = Employee()
emp3.setemployee(555,"dddd",66000)
emp3.getemployee()

print("========All Employees 1,2,3 object============")
emp1.getemployee()
emp2.getemployee()
emp3.getemployee()

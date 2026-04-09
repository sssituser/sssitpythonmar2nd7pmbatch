class Employee:
    eid : int  # static members(class variables)
    ename : str
    esal :int
    def setemployee(id,name,sal): # id , name,sal are local varibles  no self
        Employee.eid = id # set employee is static method
        Employee.ename = name
        Employee.esal = sal
        print(id)
        
    def getemployee(): # get employee static method self
        print(f'Employee ID : {Employee.eid} {id}')
        print(f'Employee Name : {Employee.ename}')
        print(f'Employee Salary : {Employee.esal}')
        
Employee.setemployee(111,'abc',60000)
Employee.getemployee()

Employee.setemployee(112,'pqr',70000)
Employee.getemployee()

Employee.getemployee()
Employee.getemployee()
# static members can be accessed using class name
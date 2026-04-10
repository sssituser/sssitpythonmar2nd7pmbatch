class Employee:
    def __init__(self,eid,ename,esal):
        print("Hi Im Constructor with Paramters")
        self.eid = eid
        self.ename = ename
        self.esal = esal
    def getemployee(self):
        print(f'Employee ID : {self.eid}')
        print(f'Employee Name : {self.ename}')
        print(f'Employee Salary : {self.esal}')

Employee(111,"abc",78888).getemployee()


emp1 = Employee(444,"ddd",666)
emp1.getemployee()
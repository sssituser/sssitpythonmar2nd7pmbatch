import mysql.connector as mysql
class PdbcExample:
    def __init__(self):
        self.connection = mysql.connect(host='localhost',user='root',password='root',db='prodb')
        self.cursor = self.connection.cursor()
    def  addemployee(self,eid,ename,esal):
        self.cursor.execute("INSERT INTO tbl_employee VALUES(%s,%s,%s)",(eid,ename,esal))
        self.connection.commit()
        print("Employee Added")
    def updateemployee(self,eid,ename,esal):
        self.cursor.execute("update tbl_employee set ename = %s , esal = %s where eid = %s",(ename,esal,eid))
        self.connection.commit()
        print("Employee updated")
    def deleteemployee(self,eid):
        self.cursor.execute("delete from tbl_employee where eid = (%s)",(eid,))
        self.connection.commit()
        print("Employee deleted")
    def findyemployeebyid(self,eid):
        self.cursor.execute("select * from tbl_employee where eid = (%s)",(eid,))
        row = self.cursor.fetchone()
        if row is not None:
            print(f'Employee ID : {row[0]} Employee Name : {row[1]}\nEmployee Salary : {row[2]}')
        else:
            print("Record Not Found")
pdbc = PdbcExample()
while True:
    choice = int(input("1.Add\n2.Delete\n3.Update\n4.Find\n5.Show All\nEnter choice : "))
    match choice:
        case 1:
            eid = int(input('Enter Employee ID : '))
            ename = input('Enter Employee Name : ')
            esal = int(input('Enter Employee Salary : '))
            pdbc.addemployee(eid,ename,esal)
        case 3:
            eid = int(input('Enter Employee ID : '))
            ename = input('Enter Employee Name : ')
            esal = int(input('Enter Employee Salary : '))
            pdbc.updateemployee(eid,ename,esal)
        case 2:
            eid = int(input('Enter Employee ID : '))
            pdbc.deleteemployee(eid)
        case 4:
            eid = int(input('Enter Employee ID : '))
            pdbc.findyemployeebyid(eid)     
        case _:
            print("Invalid choice....")        
            
        
        
            
        
    
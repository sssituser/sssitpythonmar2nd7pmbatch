import mysql.connector as mysql
connection= mysql.connect(host = "localhost",user="root",password="root",db="prodb")
cursor = connection.cursor()
eid =  int(input('Enter Employee ID : '))
ename = input('Enter Employee Namae : ')
esal = int(input('Enter Employee Salary :'))
cursor.execute("INSERT INTO tbl_employee VALUES(%s,%s,%s)",(eid,ename,esal))
connection.commit()
print("Record Inserted Successfully...")

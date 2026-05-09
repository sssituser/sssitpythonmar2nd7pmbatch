import mysql.connector as mysql
conn = mysql.connect(host='localhost',user='root',password='root',db='prodb')
cursor = conn.cursor()
def getall():
    cursor.execute("select * from tbl_employee")
    rows = cursor.fetchall()
    print("================================================")
    print("ID\t\tName\t\tSalary")
    print("================================================")
    for row in rows:
        print(f'{row[0]}\t\t{row[1]}\t\t{row[2]}')
while True:
    choice = int(input("1.Add\n2.Delete\n3.Update\n4.Find\n5.ShowAll\nEnter your choice : "))
    match choice:
        case 1:
            id = int(input('Enter Id :'))
            name = input('Enter Name : ')
            sal = int(input('Enter Salary :'))
            cursor.execute("insert into tbl_employee values(%s,%s,%s)",(id,name,sal))
            conn.commit()
            print("Record inserted")
            getall()
        case 2:
            id = int(input('Enter Id : '))
            cursor.execute("delete from tbl_employee where eid = (%s)",(id,))
            conn.commit()
            print("Record deleted")
            getall()
        case 3:
            id = int(input('Enter Id :'))
            name = input('Enter Name : ')
            sal = int(input('Enter Salary :'))
            cursor.execute("update tbl_employee set ename = %s,esal = %s where eid=%s",(name,sal,id))
            conn.commit()
            print("Record updated")
            getall()
        case 4:      
             id = int(input('Enter Id : '))   
             cursor.execute("select * from tbl_employee where eid =(%s)",(id,))   
             row = cursor.fetchone()
             print(f"Employee Name : {row[1]}\nEmployee Salary : {row[2]}")
        case 5:
             getall()
             
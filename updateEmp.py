import mysql.connector

def update(id, sal):
    conn = mysql.connector.connect(host='localhost', database = 'mydb', user = 'root', password ='password')

    if conn.is_connected():
        print('Connected to mysql db')
        cursor = conn.cursor()
        mystr = "update emp set sal = '%d'  where id = '%d' "
        args = ( sal, id)
        try:
            cursor.execute(mystr % args )
            conn.commit()
            print('Employee updated')
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

empId = int(input('Enter Emp Id : '))
empSal= int(input('Enter New Salary : '))
update(empId,empSal)
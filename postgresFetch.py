import psycopg2
#run the program with RUN not in the console

connection = psycopg2.connect(database = 'employeedb',
                              user='test',
                              password = 'password',
                              host = '127.0.0.1',
                              port = '5432')

print('Connected to EmployeeDB')

cursor = connection.cursor()
cursor.execute("select * from employee")
rows = cursor.fetchall()
for row in rows:
    print('Id', row[0])
    print('Name', row[1])
    print('Salary', row[2])



connection.close()
from connection import create_connection

class Ems:
    def __init__(self):
        self.connection = create_connection()
        self.cursor = self.connection.cursor()

    def add(self, name, MobileNumber, EmailID, Designation):
        sql = 'INSERT INTO EmployeeDetails (name, MobileNumber, EmailID, Designation) VALUES (%s, %s, %s, %s)'
        val = (name, MobileNumber, EmailID, Designation)
        self.cursor.execute(sql, val)
        self.connection.commit()
        # print(self.cursor.rowcount, "record inserted.")
        print(f"New Employee details are : \nName: {name}, \nMobileNumber: {MobileNumber}, \nEmailID: {EmailID}, \nDesignation: {Designation}\n")

    def emp(self, a):
        sql = "SELECT * FROM EmployeeDetails WHERE EmployeeID = %s"
        val = (a,)
        self.cursor.execute(sql, val)
        myresult = self.cursor.fetchall()
        if myresult:
            l = ['EmployeeID : ', '\nName : ', '\nContact Details : ', '\nEmail ID : ', '\nDesignation : ']
            for record in myresult:
                l1 = list(record)  # Converts tuple to list
            ct = 0
            for i in range(0, len(l) * 2):
                if i % 2 != 0:
                    l.insert(i, l1[ct])
                    ct += 1
            print(*l)
        else:
            print(f"No employee found with EmployeeID {a}\n")
    
    def dlt(self, a):
        sql = 'DELETE FROM EmployeeDetails WHERE EmployeeID = %s'
        val = (a,)
        self.cursor.execute(sql, val)
        self.connection.commit()

        if self.cursor.rowcount == 0:
            print(f"EmployeeID {a} not found. No details available to delete.\n")
        else:
            print(f"Employee Details of the EmployeeID {a} deleted successfully.\n")

    def all(self):
        sql = 'SELECT * FROM EmployeeDetails'
        self.cursor.execute(sql)
        a = ('EmployeeID', 'Name', 'MobileNumber', 'EmailID', 'Designation')
        re = self.cursor.fetchall()
        print(a)
        for r in re:
            print(r)
        print()
    


    def update(self,a):
        connection = create_connection()  
        cursor = connection.cursor()  # Helps to execute the SQL queries
        sql = 'SELECT Designation FROM EmployeeDetails WHERE EmployeeID = %s'
        val = (a,)
        cursor.execute(sql, val)
        re = cursor.fetchall()
        if re:
            for r in re:
                b=str(r[0])
                if b=='Employee':
                    print('Current Designation : Employee' )
                    up= 'Update employeedetails set designation="Team Lead" where employeeid=%s '
                    cursor.execute(up, val)
                    connection.commit()
                    print('After Promotion : Team Lead')
                elif b=='Team Lead':
                    print('Current Designation : Team Lead')
                    up= 'Update employeedetails set designation="Manager" where employeeid=%s '
                    cursor.execute(up, val)
                    connection.commit()
                    print('After Promotion : Manager')

                elif b== 'Manager':
                    print('Current Designation : Manager')
                    up= 'Update employeedetails set designation="Delivery Head" where employeeid=%s '
                    cursor.execute(up, val)
                    connection.commit()
                    print('After Promotion : Delivery Head')
                
                else:
                    print("No further promotion available.")
            
        else:
            print(f"No employee found with EmployeeID {a}")




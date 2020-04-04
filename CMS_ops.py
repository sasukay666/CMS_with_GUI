''''This program handles basic operations on a Customer Managaement System'''

#BLL
import pymysql

class Customer:

    Custlist=[]
    def __init__(self, name = '', address = '', mobile = ''):
        '''constuctor of Customer class to create and initialize variables of object'''
        self.id = -1
        self.name = name
        self.address = address
        self.mobile = mobile

    def addCustomer(self):
        '''addCustomer(self) takes the object as input from PL and
        runs INSERT INTO table query'''
        global con
        myCursor = con.cursor()
        strQuery = f"INSERT INTO cmscustomer (name, address, mobile) VALUES ('{self.name}', '{self.address}', '{self.mobile}')"
        rowAffected = myCursor.execute(strQuery)
        if rowAffected!=0:
            con.commit()
        else:
            raise Exception("Can't Insert Details Into Table")

    def searchCustomerByID(self):
        '''searchCustomerByID() searches for id in the cmscustomer table and returns the corresponding values'''
        myCursor = con.cursor()
        strQuery = f"SELECT * FROM cmscustomer WHERE id = {self.id};"
        rowAffected = myCursor.execute(strQuery)
        if rowAffected != 0:
            result = myCursor.fetchone()
            self.name = result[1]
            self.address = result[2]
            self.mobile = result[3]
        else:
            raise Exception("ID not Found")

    def searchCustomerByName(self):
        '''searchCustomerByID() searches for name in the cmscustomer table and returns the corresponding values'''
        myCursor = con.cursor()
        strQuery = f"SELECT * FROM cmscustomer WHERE name = '{self.name}';"
        rowAffected = myCursor.execute(strQuery)
        if rowAffected != 0:
            Customer.Custlist.clear()
            for row in myCursor.fetchall():
                cus = Customer()
                cus.id = row[0]
                cus.name = row[1]
                cus.address = row[2]
                cus.mobile = row[3]
                Customer.Custlist.append(cus)
        else:
            raise Exception("Name not Found")

    def searchCustomerByMobile(self):
        '''searchCustomerByID() searches for mobile in the cmscustomer table and returns the corresponding values'''
        myCursor = con.cursor()
        strQuery = f"SELECT * FROM cmscustomer WHERE mobile = '{self.mobile}';"
        rowAffected = myCursor.execute(strQuery)
        if rowAffected != 0:
            result = myCursor.fetchone()
            self.name = result[1]
            self.address = result[2]
            self.id = result[0]
        else:
            raise Exception("Mobile not Found")

    def updateAll(self):
        myCursor = con.cursor()
        strQuery = f"UPDATE cmscustomer SET name = '{self.name}', address = '{self.address}', mobile = '{self.mobile}' WHERE id = {self.id}"
        rowAffected = myCursor.execute(strQuery)
        if rowAffected!=0:
            con.commit()
        else:
            raise Exception("The ID you entered could not be found")

    def updateCustomerName(self):
        myCursor = con.cursor()
        strQuery = f"UPDATE cmscustomer SET name = '{self.name}' WHERE id = {self.id}"
        rowAffected = myCursor.execute(strQuery)
        if rowAffected!=0:
            con.commit()
        else:
            raise Exception("The ID you entered could not be found")

    def updateCustomerAddress(self):
        myCursor = con.cursor()
        strQuery = f"UPDATE cmscustomer SET address = '{self.address}' WHERE id = {self.id}"
        rowAffected = myCursor.execute(strQuery)
        if rowAffected!=0:
            con.commit()
        else:
            raise Exception("The ID you entered could not be found")

    def updateCustomerMobile(self):
            myCursor = con.cursor()
            strQuery = f"UPDATE cmscustomer SET mobile = '{self.mobile}' WHERE id = {self.id}"
            rowAffected = myCursor.execute(strQuery)
            if rowAffected!=0:
                con.commit()
            else:
                raise Exception("The ID you entered could not be found")

    @staticmethod
    def deleteCustomer(id):
        myCursor = con.cursor()
        strQuery = f"DELETE FROM cmscustomer WHERE id = {id}"
        rowAffected = myCursor.execute(strQuery)
        if rowAffected!=0:
            con.commit()
        else:
            raise Exception("No matching record found for the id")

    @staticmethod
    def viewAll():
        '''This viewAll() function fetches all the entries from customer table.
        The reference object of each row is saved in a static list
        This static list Custlist can be accessed in PL using class name
        to access all the entries'''
        myCursor = con.cursor()
        strQuery = "SELECT * FROM cmscustomer;"
        rowAffected = myCursor.execute(strQuery)
        if rowAffected!=0:
            Customer.Custlist.clear()
            for row in myCursor.fetchall():
                cus = Customer()
                cus.id = row[0]
                cus.name = row[1]
                cus.address = row[2]
                cus.mobile = row[3]
                Customer.Custlist.append(cus)
        else:
            raise Exception("Table is Empty.")

    @staticmethod
    def login(host, user, password):
        '''This function takes host, user name and password from
        the user and creates a conncection using pymysql class'''
        global con
        con = pymysql.connect(host=host, user=user, password=password, database='cms_customer')

    global host, user, password             #global variables to allow access of database from all the implemented functions
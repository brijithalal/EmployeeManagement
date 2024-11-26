import mysql.connector

class DBConnect:
    def __init__(self,host="localhost",user="root",password="root",database="employeemanagement"):
        # self.connection =None
        self.host=host
        self.user=user
        self.password=password
        self.database = database

    def connection(self):
        self.connection=mysql.connector.connect(
            host =self.host,
            user=self.user,
            password = self.password,
            database = self.database
        )

        if self.connection.is_connected():
            print("connected to mysql")


    def disconnect(self):
        if self.connection and self.connection.isConnected():
            self.connection.close()
            print("Disconnected")

    # def  create_database(self,database_name):

objConnect = DBConnect(host="localhost",user="root",password="faith",database="employeemanagement")
objConnect.connection()



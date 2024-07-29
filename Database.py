import mysql.connector as connector

class Database:
    def __init__(self,username,password):
        try:
            self.__connection = connector.connect(user=username, password=password);
            self.cursor = self.__connection.cursor()
            self.cursor.execute('USE SMS')
        except connector.Error as err:
            print("Error:",err.msg)
    def __del__(self):
        if self.__connection.is_connected():
            self.__connection.close()
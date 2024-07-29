from Database import Database

class StudentManagementSystem:
    def __init__(self):
        self.__database = Database('root','')
    def login(self,username,password):
        self.__database.cursor.execute(f"""SELECT * FROM users WHERE username = "{username}" """)
        record = self.__database.cursor.fetchall()
        if len(record) < 1:
            return (False, 'User not found')
        elif record[0][3] != password:
            return (False, 'Invalid Password')
        return (True, record[0])
from App import StudentManagementSystem as SMS

app = SMS()
def main():
    username = input('Enter Username:')
    password = input('Enter Password:')
    auth = app.login(username,password)
    if auth[0]:
        print('Hello,',auth[1][1])
    else:
        print(auth[1])
main()
import user

def choose():
    print("1.Register")
    print("2.Login")
    print("3.Forgot Password")
    return input()

while True:
        user_input = choose()
        if user_input=='1':
            user.register()
        elif user_input=='2':
            user.login()
        elif user_input=='3':
            user.reset_password()
        else:
            print("Choose a valid option")
            continue

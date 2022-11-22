import pickle
import checker as check
import os

def getemail():
    print("Enter email")
    return input()

def getpassword(reset=False):
    if reset==False:
        print("Enter password")
    else:
        print("Enter new password")    
    return input()

def register():
    email=getemail()
    if check.check_email(email) is False:
        print("Invalid email, must be of the form example@email.com")
        return 

    user_cred={}

    if os.path.isfile("user_cred.txt"):
        f = open("user_cred.txt","rb")
        user_cred = pickle.load(f)
        f.close()  
    if email in user_cred.keys():
        print("user already exists, try logging in")
        return
    else:
        password=getpassword()
        while check.check_password(password) is False:
            print("Invalid password, must contain at least one uppercase, lowercase, digit, a special character, and 5<length<16:")
            password=getpassword()
        f=open("user_cred.txt","wb")
        user_cred[email]=password   
        pickle.dump(user_cred,f)
        print("user registered")
        f.close()

def login():
    email=getemail()

    if os.path.isfile("user_cred.txt"):
        f=open("user_cred.txt","rb")
        users = pickle.load(f)
        f.close()
        if not email in users.keys():
            print("user doesn't exist, register now")
        else:
            password=getpassword()
            if users[email]==password:
                print("login successful")
            else:
                print("wrong password")    
    else:
        print("empty database")            

def reset_password():
    email=getemail()
    if os.path.isfile("user_cred.txt"):
        f=open("user_cred.txt","rb")
        user_cred=pickle.load(f)
        f.close()
        if email in user_cred.keys():
            print("1.Get Password\n2.Reset Password")
            user_input=int(input())
            if user_input==1:
                f=open("user_cred.txt","rb")
                print("your password: " + user_cred[email])
                f.close()
            elif user_input==2:
                reset_password=getpassword(True)
                if not check.check_password(reset_password):
                    print("Invalid password, must contain at least one uppercase, lowercase, digit, a special character, and 5<length<16")
                    return
                else:
                    f=open("user_cred.txt","wb")    
                    user_cred[email]=reset_password
                    pickle.dump(user_cred,f)
                    print("password changed")
                    f.close()
            else:
                print("invalid option")    
        else:
            print("user doesn't exist, register now")
    else:
        print("empty databse")    

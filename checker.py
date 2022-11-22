def check_email(email):
    if email.count('@')==1 and email.count('.')==1 and email.find('.')>email.find('@'):
        split_dot=email.split('.') 
        split_at=split_dot[0].split('@')
        if len(split_at[0])>=1 and len(split_at[1])>=1 and len(split_dot[1])>=1 and split_at[0][0].isalpha():
            return email
    return False

def check_password(password):
    checks={
        "upper":False,
        "lower":False,
        "digit":False,
        "special":False
    }
    if len(password)>5 and len(password)<16:
        for ch in password:
            if ch.isalpha() and ch.isupper():
                checks["upper"]=True
            elif ch.isalpha() and ch.islower():
                checks["lower"]=True
            elif ch.isdigit():
                checks["digit"]=True
            else:
                checks["special"]=True 
        if not False in set(list(checks.values())):
            return password
    return False                                

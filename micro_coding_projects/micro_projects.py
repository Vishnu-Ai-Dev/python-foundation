'''def check_user(age):
    if age<13:
        return ("child")
    elif age>13:
        return("adult")
    elif age>=60:
        return ("Senior")
    else:
        return("Invalid age")
print(check_user(18))'''

def is_allowed(user_type):
    if user_type>13:
        return("True")
    elif user_type<=13:
        return("False")
    elif user_type>60:
        return("True")
    else:
        return("Invalid age")
print(is_allowed(18))

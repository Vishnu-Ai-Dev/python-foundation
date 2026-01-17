#day 8 intermediate level of python started

'''print("day 8-functions and parameters started")'''

#understanding the basic syntax of functions

'''def greet():
     print("carpedium!")'''

#using the parameters we are going to input the values

'''def greet(name):
    print("welcome",name)
user_name=greet("vishnu")
print(user_name)'''
    
#calling the functions using return to use that code repeatedly without breaking the ouput

'''def math(a,b):
    return(a+b)
result=math(3,4)
print(result)'''

#mini practise code (1)

'''def square(n):
    return n*n
print(square(4))'''

#mini practise code (2)

'''def is_even(n):
    return n%2==0
print(is_even(8))'''

#Real world application finding the age through functions

'''def age(n):
    if n<=15:
        return "CHILD"
    elif n<=24:
        return "ADULT"
    else:
        return "SENIOR"
print(age(10))
print(age(12))
print(age(45))
print(age(18))'''

#Real world application mark grade system

'''def stud_marks(n):
    if n<25:
        return "Fail"
    elif n<=50:
        return "C"
    elif n<=75:
        return "B"
    elif n<=100:
        return "A"
    else:
        return "Invalid mark please enter a vaild one"
print(stud_marks(24))
print(stud_marks(224))
print(stud_marks(54))
print(stud_marks(97))
print(stud_marks(34))'''

# Real world application building a scalable auth system using functions

def login(user,password):
    if user=="admin"and password=="root1234":
        return "admin access entering the admin mode"
    elif user=="admin" and password!="root1234":
        return "you are not an admin please enter a valid one"
    elif user=="user" and password=="user1234":
        return "user access! welcome to user mode"
    elif user=="user" and password!="user1234":
        return "incorrect password"
    else:
        return "new user detected please sign in with a new account"
print(login("admin","root1234"))
print(login("admin","user1234"))
print(login("user","user1234"))
print(login("user","132ty7"))
print(login("hflhf","34iof"))
    

#wrting a file using the w and checking how the content is written

'''with open("user.txt","w") as file:
    file.write("user: Ranpo\n")
    file.write("user: Gilgamesh\n")'''

#appending a text using "a" and unserstanding how logs are added

'''with open("Log.txt","a") as file:
    file.write("throughout the heaven and earth I alone the honoured one\n")
    file.write("Nah i'd win")'''

#reading from a file
'''with open("user.txt", "r") as file:
    content=file.read()
    print(content)'''


#creating a super marker storing systems
'''with open("online_customer,txt","w") as file:
    print("               welcome to hallmart shopping        ")

    cust_name=input("Enter your name:")
    cust_address=(input("Enter your adress:"))

    file.write(cust_name+"\n")
    file.write(cust_address+"\n")'''

'''def login_system(user,pass_word):
    if user=="admin" and pass_word=="admin123":
        return ("Admin access allowed")
    elif user=="admin":
        return ("Invalid password")
    elif user=="user" and pass_word=="user123:":
        return ("user access allowed")
    elif user=="user":
        return ("Wrong password")
    else:
        return("New user Detected")
user_name=input("Enter name:")
password=(input("enter password:"))
print(login_system(user_name,password))

with open("login system.txt","w") as file:
    file.write(user_name +" Attempted login"+"\n")'''


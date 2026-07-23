#### Q1.Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

# lets assign a id and password itself.
id="@harshal"
password="@1234"

# lets take id and password from user to check:
i_d=input("Enter id:")

pass_w=input("Enter password:")

if i_d==id and password==pass_w:
    print("login successfully!")
else:
    for i in range(1,4):
        i_d=input("Enter id:")
        pass_w=input("Enter password:")
        if i_d==id and password==pass_w:  # in betn that 3 try if  user enters valid id and pass it will login
            print("login successfully!")
            break
    else:
        print("invalid id and pass! try after some time.")    
        

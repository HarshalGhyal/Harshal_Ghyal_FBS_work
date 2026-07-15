#### Q7.Write a program to check if user has entered correct userid and password.

# lets set a user id and password:
u_id="harshal"
pasw="@123"


# lets take two input as a user_id and password.

user_id=input("enter user id:")

password=input("enter password:")

# lets check:
if u_id==user_id and pasw==password:
    print("login successfully!")
else:
    print("login failed!,please enter correct userid and password.")    
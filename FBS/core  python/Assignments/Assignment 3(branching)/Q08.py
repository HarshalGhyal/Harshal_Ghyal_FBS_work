#### Q8.Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha).

import random
# lets set a user id and password:
u_id="harshal"
pasw="@123"


# lets take two input as a user_id and password.

user_id=input("enter user id:")

password=input("enter password:")

# lets check:
if u_id==user_id and pasw==password:
    captch=random.randint(1000,9999)
    
    print("Captcha:",captch)
    captcha=int(input("please enter given captcha:"))
    if captch==captcha:
        print("login successfully!")
    else:
        print("enter given captcha!,you entered wrong captcha..login failed")
else:
    print("please enter correct userid and password!")            
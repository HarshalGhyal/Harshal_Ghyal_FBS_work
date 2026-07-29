# 1. pass: To neglet expected indentation error
for i in range(1,10):
    pass

# 2.break: To terminate the loop
for i in range(1,11):
    if(i==3):
        break
    print(i)

#3.continue: To stop current iteration only.
for i in range(1,10):
     if(i==3):
        continue
     print(i)

# 4.else: will execute when loop executed successfully.
for i in range(1,5):
    if(i==3):
        break
else:
    print("code executed successfully !")         
   
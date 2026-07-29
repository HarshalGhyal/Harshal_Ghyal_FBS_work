# if we have multiple condition that one of them is can be true we use elseif.
# for e.g: here number can be either -ve,+ve or 0.
num=int(input("enter number:"))

if num==0:
    print("neutral!")
elif num>0:
    print('positive number!')   
else:
    print("Negative number!")     
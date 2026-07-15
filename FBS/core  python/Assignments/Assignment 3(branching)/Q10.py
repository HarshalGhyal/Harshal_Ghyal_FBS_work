#### Q10.Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender=input("enter gender(m/f):")
age=int(input("enter age:"))

if(gender=='f'):
    if(age>=18):
        print("girl is eligible for marriage")
    else:
        print("girl is not eligible for marriage") 
elif(gender=='m'):
    if(age>=21):
        print("boy is eligible for marriage") 
    else:
        print("boy is not eligible")
else:
    print("please enter m or f for male or female!")                 

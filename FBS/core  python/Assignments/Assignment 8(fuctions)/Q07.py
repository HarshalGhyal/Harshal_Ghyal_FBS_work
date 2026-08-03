#### Q7.Write a program to find sum of digits of a number.


def sum_of_digits():
    num=int(input("Enter number:"))
    sum=0
    
    while(num>0):
        d=num%10
        sum+=d
        num=num//10
    return sum    

c=sum_of_digits()
print(c)





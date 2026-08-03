#### Q10.Write a program to reverse a number using recursion.

def rev(num,sum=0):
    if num==0:
        return sum
    digit=num%10
    sum=sum*10+digit
    return rev(num//10,sum)

num=int(input("Enter number:"))
a=rev(num)
print(a)
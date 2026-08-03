#### Q7.Write a program to find sum of digits using recursion.

def sum_of_digits(num,sum=0):
    if num==0:
        return sum
    digit=num%10
    sum=sum+digit
    return sum_of_digits(num//10,sum)

num=int(input("Enter number:"))
a=sum_of_digits(num)
print(a)

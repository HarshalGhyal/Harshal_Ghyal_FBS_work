#### Q1. Write a program to find sum of following series using recursive functions:
#         i. 1! + 2! + 3! + 4! +..... + n!
# Note : For fact and sum two recursive functions


def factorial(z):
    if z>0:
        return z*factorial(z-1)
    else:
        return 1


def sum_of_f_series(n):
    sum=0
    for z in range(1,n+1):
        sum+=factorial(z)
    return sum       

n=int(input("enter the last element of series:")) 

s=sum_of_f_series(n)
print(s)
       
    





    
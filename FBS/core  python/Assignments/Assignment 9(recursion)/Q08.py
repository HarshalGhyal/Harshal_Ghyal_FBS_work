####Q8.Write a program to check whether a number is prime or not using recursion.

def prime(num,n):
    if num<=1:
        return False
    elif n==1:
        return True
    elif num%n==0:
        return False
    return prime(num,n-1)


def is_prime(num):
    if prime(num,num//2):
        print(f"{num} is prime a number")
    else:
        print(f"{num} is not a prime number")    
        

num=int(input("Enter number:"))           

is_prime(num)
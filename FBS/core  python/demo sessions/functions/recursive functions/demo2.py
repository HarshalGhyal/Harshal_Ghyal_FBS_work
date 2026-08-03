#### wap factorial
def factorial(n):
    if n>0:
        return n*factorial(n-1)
    else:
        return 1

n=5
s=factorial(n)  
print(s)  
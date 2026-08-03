#### Q4.Write a program to find sum of n numbers using recursion.

def sum_of_series(n):
    if n>0 :
        return n + sum_of_series(n-1)
    else:
        return 0
n=int(input("Enter last number of series:"))
res=sum_of_series(n)
print(res)    
    



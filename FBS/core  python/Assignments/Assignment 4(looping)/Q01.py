#### Q1. WAP to print all even numbers until n.

# lets take input as n for printing even number until n:
n=int(input("enter the number until you want to print even numbers:"))
#lets print even numbers:
for i in range(0,n+1):   # or we can take range(0,n+1,2) and then print(i)
    if i%2==0:
        print(i)
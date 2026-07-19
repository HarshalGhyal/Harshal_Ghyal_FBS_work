#### Q2.WAP to print all odd numbers until n.

# lets take input as n for printing odd number until n:
n=int(input("enter the number until you want to print odd numbers:"))
#lets print odd numbers:
for i in range(1,n+1,2):   # or we can take range(1,n+1,2) and then print(i)
    if i%2!=0:
        print(i)
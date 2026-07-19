#### Q8.WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

# lets take input as n
n=int(input("Enter range(1 to n):"))

# lets iterate:
for i in range(1,n+1):
    if i%7==0 and i%5==0:
        print(i)
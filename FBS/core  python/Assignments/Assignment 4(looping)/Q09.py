#### Q9.WAP to print all numbers in a range divisible by a given number.

# lets take input a n as range and num 
n=int(input("Enter range:"))

num=int(input("Enter number to divide:"))

#lets iterate:
for i in range(1,n+1):
    if i%num==0:
        print(i)
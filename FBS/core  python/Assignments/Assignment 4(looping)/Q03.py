#### Q3.WAP to print sum of series upto n.

# lets take n as a input:
n=int(input("Enter the ending number of series:"))
# lets initialize the var to store sum of numbers until n.
sum=0

# so if which seies is not mention like n^2 or n lets print it for n only.
for i in range(0,n+1):
    sum=sum+i
print(f"The sum of series until {n} is {sum}")    


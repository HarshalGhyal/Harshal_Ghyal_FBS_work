#### Q10.WAP to check if given number is Perfect Number.

# note: the perfect number is +ve integer that is exacly equal to sum of its proper +ve divisors.

# lets take input as a number.
num=int(input("Enter number:"))

# lets initialize var sum and is_perfect
sum=0
is_perfect=True

#lets  iterate
if num<=1:
    is_perfect=False
for i in range(1,num):
    if num%i==0:
        sum=sum+i
        if sum==num:
            is_perfect=True
            break
        else:
            is_perfect=False
if is_perfect==True:
    print(f"{num} is perfect number !")
else:
     print(f"{num} is not a perfect number !")
        


            


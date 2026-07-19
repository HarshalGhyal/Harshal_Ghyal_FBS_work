#### Q11.WAP to check if given number Strong Number.

# Note:A Strong Number  is a number whose sum of the factorials of its digits is equal to the number itself.

#lets take input as a num
num=int(input("Enter number:"))
temp=num
#lets initalize var sum 
sum=0

#lets iterating with while for seperating digits.
while(num>0):
    d=num%10
    # lets initialize fact inside while becoz with every fact value gonna be change but we want fact=1 for every digit to factorize.
    fact=1
    # lets write for loop for factorial of seperated digits
    for i in range(d,0,-1):
        fact*=i
    
    #lets add every factorial of sep digit in sum
    sum=sum+fact
    # move on to find next sep digit
    num=num//10


#comparing sum with num itself to check it is a stong number or not.
if sum==temp:
    print(f"{temp} is a strong number !")
else:
    print(f"{temp} is not a strong number !")     
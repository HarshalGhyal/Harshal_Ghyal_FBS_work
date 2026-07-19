#### Q6.WAP to check if a given number is prime number or not.

# lets take input as a number.
num=int(input("Enter number:"))

#lets initialize var
is_prime=True
# lets  iterate:
if num<=1:
    is_prime=False
    
else:    
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
        
    
if is_prime==True:
    print(f"{num} is prime number") 
else:
    print(f"{num} is not prime number")               
        
   
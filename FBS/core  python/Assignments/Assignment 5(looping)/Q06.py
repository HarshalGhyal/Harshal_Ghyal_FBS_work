#### Q6. Write a program to print first n prime numbers.

#lets take n as a input
n=int(input("Enter last n number you want to print:"))

#lets iterate
for num in range(n+1):
    if(num>1):
        for i in range(2,num//2+1):
            if(num%i==0):
                break
        else:
            print(num)
    else:
        print(f'{num} is not prime number nor composite !')            




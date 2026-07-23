#### Q5.Write a program to print prime numbers between 1 to 100.

#lets iterate 1 to 100:
for num in range(1,101):
    if(num>1):
        for i in range(2,num//2+1):
            if(num%i==0):
                break
        else:
            print(num)
    else:
        print(f'{num} is not prime number nor composite !')            





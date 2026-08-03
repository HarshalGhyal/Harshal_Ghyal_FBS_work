#### Q3.Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n

def sum_of_series():
    # lets take n common for all series.
    n=int(input("Enter last element of series you want to print:"))

    # lets calculate: a. 1+ 2 + 3 + 4+..... + n first:
    print(f" a. 1+ 2 + 3 + 4+..... + {n} :")
    #lets initialize var total to add all series.
    total=0
    #lets iterate untill n:
    for i in range(1,n+1):
        total+=i
    print(f"The solution for sum of series a. until {n} is {total}")    

    # lets calculate: b. 1!+ 2! + 3! + 4!+..... + n! second:
    print(f'\n b. 1!+ 2! + 3! + 4!+..... + {n}! :')
    #lets initialize var total to add all factorials of numbers until n.
    total=0
    #lets iterate ,the outer loop will give us no. until n to find its factorial.
    for num in range(1,n+1):
    #lets initialize fact=1 in loop so for every interation it holds same value and not change
        fact=1
   #the inner loop will calculate factorial of num and save it in fact.
        for j in range(1,num+1):
            fact*=j

        # every factorial will add to total to calculate given series   
        total+=fact
        
    print(f"The solution for factorial series b. until {n} is {total}")

    #lets calulate: c. 1^1 + 2^2 + 3^3+ ...... n^n
    print(f'\nc. 1^1 + 2^2 + 3^3+ ...... {n}^{n}')
    #lets initialize var total to add all series.
    total=0
    # lets iterate until n:
    for i in range(1,n+1):
        total+=(i**i)
    print(f"The solution for sum of series c. until {n} is {total}")    

sum_of_series()        











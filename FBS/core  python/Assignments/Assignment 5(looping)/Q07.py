#### Q.7.Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!
# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

# lets take input a n because all given series we have to print untill n.
n=int(input("Enter a number or the range(last element(place) of series you want print:"))


##  a. 1! + 2! + 3! + 4! + .....n! first also k/a factorial series.

print(f"a. 1! +  .....{n}! :")
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
        
print(f"The solution for factorial series a. until {n} is {total}")


## b.N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent) for second.

print(f"\nb. N + N^2 + N^3+N^4 .....+N^{n}:")

# lets take input as N
N=int(input("please Enter starting no. of series:"))
#lets initialize var total to save sum of series.
total_b=0
#lets iterate
for num in range(1,n+1):
    no_s=N**num
    total_b+=no_s

print(f"The solution for given series b. until {n} is {total_b}")    


##  c.Find the sum of a geometric series from 1 to n where the common ratio is 2.

print(f"\nc.the sum of a geometric series from 1 to {n} where the common ratio is 2.")

#lets initialize 2 var r for common ratio and total_c for sum of series.
total_c=0 
r=2

#lets iterate:
for no in range(1,n+1):
    no_g=r**(no-1)
    total_c+=no_g

print(f"The solution for given series b. until {n} is {total_c}")


##  d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10.

print("\nd.S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10 :")

# lets take total and d=10 because we are not tell to print until n
d=10
total_d=0
# lets take input as a c.
a=int(input("please enter starting number:"))
#lets iterate.
for i in range(1,d+1):
    s=(a**i)/i
    total_d+=s
print(f"The solution for given series d. until 10 is {total_d}") 


##  e. x - x2/3 + x3/5 - x4/7 + .... to n terms.

print(f"\ne.x - x2/3 + x3/5 - x4/7 + .... to {n} terms")

# lets take input  as x value.
x=int(input("Enter value for x :"))
#lets initialize var total_e,den as denominator and sign to make -ve value +ve.
den=1
sign=1
total_e=0
# lets iterate.
for i in range(1,n+1):
    total_e+=sign*((x**i)/den)
    den+=2
    sign*=-1

print(f"The solution for given e. series until {n} is {total_e}")    

    







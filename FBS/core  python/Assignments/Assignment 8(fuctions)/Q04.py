#### Q4.Sum of all odd numbers between 1 to n.

def odd_num(n):
    total=0
    for i in range(1,n+1):
        if i%2!=0:
            total+=i
    return total
n=int(input("Enter last no. of series you want print:"))
a=odd_num(n)
print(f"\nsum of odd numbers from 1 to {n} is {a}")        
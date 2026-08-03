#### Q5.Sum of all prime numbers between 1 to n.

def prime_num(n):
    for num in range(n+1):
        if(num>1):
            for i in range(2,num//2+1):
                if(num%i==0):
                    break
            else:
                print(num)
        else:
            print(f'{num} is not prime number nor composite !')            

prime_num(23)

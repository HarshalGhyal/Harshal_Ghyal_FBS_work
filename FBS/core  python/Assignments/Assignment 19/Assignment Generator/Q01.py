#### Q1. We want to generate Fibonacci numbers up to a certain limit.
# Instead of computing and storing the entire sequence in memory,
# create generator to yield Fibonacci numbers one by one,
# conserving memory and allowing for easy iteration.

def fibbonacii():
    

    #lets iniatialize var a and b.
    a=-1
    b=1 # why a is -1 and b is 1 because 1st fibonnaci number is 0.

    # lets iterate:
    for i in range(1001):
        c=a+b
        yield c
        a=b
        b=c

g=fibbonacii()        
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
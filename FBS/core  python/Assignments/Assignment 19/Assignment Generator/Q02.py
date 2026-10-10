#### Q.2. Implement a generator function that yields palindrome numbers.
# Palindromes are numbers that read the same backward as forward
# (e.g., 121, 1331). Generate palindromes lazily and infinitely.


def palindrome():
    for n in range(1, 1_000_001):
        if str(n) == str(n)[::-1]:
            yield n
p=palindrome()
print(next(p))            
print(next(p))            
print(next(p))            
print(next(p))            
print(next(p))            
print(next(p))            
print(next(p))            
print(next(p))            
print(next(p))            
print(next(p))            
print(next(p))            
print(next(p))            
print(next(p))            
print(next(p))            
print(next(p))            
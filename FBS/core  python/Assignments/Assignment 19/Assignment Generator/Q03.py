#### Q3. Write a generator function that mimics the behavior of the built-in
# range() function. The generator should take start, stop, and step
# arguments and yield numbers within the specified range.


def custom_range(start, stop, step=1):
    if step == 0:
        raise ValueError("range() arg 3 must not be zero")
        
    current = start
    
    if step > 0:
        while current < stop:
            yield current
            current += step
    else:
        while current > stop:
            yield current
            current += step

# Testing the custom generator
p = custom_range(1, 45, 2)
print(next(p))  # 1
print(next(p))  # 3
print(next(p))  # 5
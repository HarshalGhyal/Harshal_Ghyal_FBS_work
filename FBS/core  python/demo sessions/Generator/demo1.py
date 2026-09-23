def demo(n):
    yield n*n
    yield n*n*n
    yield n*n*n*n
g=demo(4)
print(g.__next__())
print(g.__next__())
print(g.__next__())

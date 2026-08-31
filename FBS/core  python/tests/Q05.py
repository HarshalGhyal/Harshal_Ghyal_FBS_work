A = [1, 2, 3, 4]
B = [3, 4, 5, 6]

U = []

for i in A:
    if i not in U:
        U.append(i)

for i in B:
    if i not in U:
        U.append(i)

print(U)

li=[33,54,67,89,123,345,67,90]

max=li[0]
for ind in range(1,len(li)):
    if li[ind]>max:
        max=li[ind]
print(max)
       
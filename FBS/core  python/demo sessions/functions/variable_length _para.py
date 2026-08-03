
def add(*num):
    sum=0
    for i in num:
        sum+=i
    return sum

res=add(10,20,30,40,50,60)   
print("addition:",res)
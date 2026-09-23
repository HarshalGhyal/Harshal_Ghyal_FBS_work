dict1={}
a=int(input('Enter start:'))
b=int(input('enter end:'))

for i in range(a,b+1):
    dict1[i]=i*i
print(dict1)   
print('--------------------------------comprehension----------------------------------------------------------')
dic={i:i*i for i in range(a,b+1)}
print(dic)
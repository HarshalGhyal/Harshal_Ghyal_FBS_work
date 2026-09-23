li1=[2,3,6,8,9]
newli=[x**3 for x in li1]
print(li1)
print(newli)



a=int(input('Enter start:'))
b=int(input('enter end:'))

li1=[]

for i in range(a,b+1):
    li1.append(i**0.5)
print(li1)    
print('----------------------------------------------------------------------------------------------------------------------------------')
li2=[x**0.5 for x in range(a,b+1)]
print(li2)
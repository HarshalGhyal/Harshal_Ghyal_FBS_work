a=int(input('Enter start:'))
b=int(input('enter end:'))

li1=[]

for i in range(a,b+1):
    if i%2!=0:
        li1.append(i**2)
print('------------------------------traditionalway----------------------------------------------------------------')
print(li1) 
print('--------------------------comprehension------------------------------------------------------')
li2=[x**2 for x in range(a,b+1) if x%2!=0]
print(li2)

li7=[]


for i in range(a,b+1):
    li7.append(li2)
print(li7)    
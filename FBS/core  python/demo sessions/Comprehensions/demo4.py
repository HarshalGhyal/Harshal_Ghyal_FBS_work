
a=int(input('Enter start:'))
b=int(input('enter end:'))
li1=[]
for i in range(a,b+1):
    if i%2==0:
        li1.append('Even')
    else:
        li1.append('odd')    
print(li1)   



print('--------------------------comprehension----------------------------------------')

li2=['even' if i%2==0 else 'odd' for i in range(a,b+1)]
print(li2)



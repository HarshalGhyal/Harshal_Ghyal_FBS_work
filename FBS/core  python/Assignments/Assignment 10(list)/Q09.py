#### Q9. Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

def list_even_odd(li,even=[],odd=[]):
    even=[]
    odd=[]
    for i in li:
        if i%2==0:
            even+=[i]
        else:
            odd+=[i]    
    print('Even number list:',even)
    print('odd number list',odd)        

li=[1,2,3,4,5,6,7,8,9,10]
list_even_odd(li)
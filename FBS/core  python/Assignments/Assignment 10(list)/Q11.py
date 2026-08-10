#### Q11. Write a program to print all numbers which are divisible by m and n in the list.


def div_m_n(li):
    m=int(input("Enter m:"))
    n=int(input("Enter n:"))
    lit=[]
        
    for i in li:
        if i%m==0 and i%n==0:
            lit+=[i]
    li=lit
    print(li) 

li=[10,15,30,47,78,90,30,2230,440,345,675]  
div_m_n(li)       
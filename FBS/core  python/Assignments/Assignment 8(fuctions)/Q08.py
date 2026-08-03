#### Write a program find reverse of a number

def rev():
    num=int(input("Enter number:"))
    r_num=0
    while(num>0):
        d=num%10
        r_num=r_num*10+d
        num=num//10
    return r_num    

c=rev()
print(c)
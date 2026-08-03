#### Q9.Write a program to check if entered number is a palindrome or not.

def is_pall():
    num=int(input("Enter number:"))
    temp=num
    r_num=0
    while(num>0):
        d=num%10
        r_num=r_num*10+d
        num=num//10
    if r_num==temp:
        return f"\n{temp} is palindrome !"  
    else:
        return  f"\n{temp} is not palindrome !"


c=is_pall()
print(c)
#### Q12.Write a program to check if given 3 digit number is a palindrome or not.

# lets take input as a three digit number:
num=input("Enter number:")
# lets reverse it:
if len(num)==3:
    num=int(num)
    d1=num%10
    a=num//10
    d2=a%10
    d3=a//10
    r_num=d1*100+d2*10+d3
    if num==r_num:
        print('given number is palindrome!')
    else:
        print("given number is not pallindrome!")    

else:
    print("please enter 3 digit number!")


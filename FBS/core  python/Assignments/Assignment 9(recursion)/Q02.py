####Q2. Write a program to check if given number is Armstrong or not using recursive function.

def armstrong_sum(num,length):
    if num==0:
        return 0
    else:
        digit=num%10
        return (digit**length)+armstrong_sum(num//10,length)


def is_armstrong():
    num=int(input("Enter number:"))
    length=len(str(num))
    sum=armstrong_sum(num,length)
    if num==sum:
        print(f'{num} is an armstrong number !')
    else:
        print(f'{num} is not an armstrong number !')



is_armstrong()      

#### Q11.WAP to check if a given number is Armstrong number or not. For each task create separate functions.

def length_of_num(num):
    l = len(str(num))
    return l


def sum_of_num_with_exp(num):
    temp = num
    sum = 0

    l = length_of_num(num)      

    while(num > 0):
        d = num % 10
        mul = d ** l            
        sum = sum + mul
        num = num // 10

    return sum


def is_armstrong(num):
    summ = sum_of_num_with_exp(num)
    if num == summ:
        return f"{num} is an armstrong number!"
    else:
        return f"{num} is not an armstrong number!"


num = int(input("Enter number:"))
c = is_armstrong(num)
print(c)


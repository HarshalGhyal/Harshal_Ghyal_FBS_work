#### Q1. Python Program to Put Even and Odd elements of a List into two Different Lists.

def even_odd(li):
    even=[]
    odd=[]
    for i in li:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return f"Even number list: {even} \nOdd number list: {odd}"
    # print('Even list:',even) 
    # print('Odd list:',odd)           

li=[2,23,34,45,67,89,12,24,46,86]
print(even_odd(li))

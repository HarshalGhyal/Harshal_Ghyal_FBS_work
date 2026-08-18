#### Q15.Python Program to find larger string without using built-in functions.

str1='harshal'
str2='prathmesh'
def larger_string(str1,str2):
    count1=0
    count2=0
    for i in str1:
        count1+=1
    for j in str2:
        count2+=1

    if count1>count2:
        return f'Larger string in both given string is {str1}'
    elif count1==count2:
        return f'Both strings have same length..'    
    else:
        return f'Larger string in both given string is {str2}'          

res=larger_string(str1,str2)
print(res)

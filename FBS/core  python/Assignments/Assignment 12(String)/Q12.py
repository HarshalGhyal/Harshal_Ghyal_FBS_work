#### Q12. Python Program to count number of lowercase characters in a string.

str='HarshaL is StudenT' 
def count_lower(str):
    count=0
    for i in str:
        if (i.islower()):
            count+=1

    return count

res=count_lower(str)   
print(res)   
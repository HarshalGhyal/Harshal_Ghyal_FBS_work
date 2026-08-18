#### Q.10.Python Program to Take in Two Strings and Display the Larger String
# without Using Built-in Functions


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
        print(str1) 
    elif count1==count2:
        print(str1)
        print(str2)
    else:
        print(str2)           

larger_string(str1,str2)
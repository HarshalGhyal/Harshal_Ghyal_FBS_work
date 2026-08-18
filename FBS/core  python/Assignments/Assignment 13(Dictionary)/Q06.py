#### Q6. Python Program to Multiply All the Items in a Dictionary

dic={'a':3,'b':4,'c':6}

def add_values(dic):

    li=dic.values()
    count=1
    for i in li:
        count*=i
    return count   


res=add_values(dic)
print(res)
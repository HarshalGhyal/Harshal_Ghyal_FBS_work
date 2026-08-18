#### Q5. Python Program to Sum All the Items in a Dictionary

dic={'a':30,'b':40,'c':60}

def add_values(dic):

    li=dic.values()
    count=0
    for i in li:
        count+=i
    return count   


res=add_values(dic)
print(res)
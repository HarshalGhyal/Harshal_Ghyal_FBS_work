#### Q2. Python Program to Concatenate Two Dictionaries Into One

def add_dict(dic1,dic2):
    dic1.update(dic2)
    return dic1

dic1={'name':'harshal'}
dic2={'age':21}
res=add_dict(dic1,dic2)
print(res)
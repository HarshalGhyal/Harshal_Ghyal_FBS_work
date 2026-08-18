#### Q4. Python Program to Form a New String where the First Character and the Last Character have been Exchanged
def replace_first_last(str):
    st=list(str)
    st[0],st[-1]=st[-1],st[0]
    str2=''.join(st)
    return str2


str='harshal'
res=replace_first_last(str)
print(res)
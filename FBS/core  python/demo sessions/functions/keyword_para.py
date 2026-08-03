def emp(id,name,sal,dept):
    data='ID:'+ str(id) +'\n'
    data+='NAME:'+ str(name) +'\n'
    data+='SALARY:'+ str(sal)+'\n'
    data+='DEPARTMENT:'+ str(dept) +'\n'
    return data

res=emp(name='ABC',id=103,dept='IT',sal=300000)
print(res)
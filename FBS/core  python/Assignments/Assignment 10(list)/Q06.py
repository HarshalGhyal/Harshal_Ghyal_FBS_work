#### Q6.Write a program to remove duplicates from the list.


def rem_dupli(li):
    new = []
    new1=[]

    for ele in li:
        count = 0

        for i in li:
            if ele == i:
                count += 1

        if count == 1:
            
            new += [ele]
        elif count>=2:
            if ele not in new1:
                new1+=[ele]
            
    li=new+new1
    return li

li = [50,60,30,20,10,70,30,90,30]
a=rem_dupli(li)
print(a)
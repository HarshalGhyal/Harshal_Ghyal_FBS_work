#### Q6.Python Program to Calculate the Length of a String Without Using a Library Function
def length_of_string(str):
    count=0
    for i in str:
        count+=1
    return count


st='prathamesh'
res=length_of_string(st)
print(res)
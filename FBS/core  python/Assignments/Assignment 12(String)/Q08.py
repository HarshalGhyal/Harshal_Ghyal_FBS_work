#### Q8.Python Program to Remove the Characters of Odd Index Values in a String


def rem_oddindex(str):

    str2=''
    for i in range(len(str)):
        if i%2==0:
            str2+=str[i]

    return str2


st='harshal'
res=rem_oddindex(st)
print(res)

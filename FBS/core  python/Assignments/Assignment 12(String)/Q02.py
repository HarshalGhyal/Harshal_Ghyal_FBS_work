#### Q2.Python Program to Remove the nth Index Character from a Non-Empty String.

def remove_index(str,str2=''):
    ind=int(input("Enter the index of char you want to remove:"))

    ele=str[ind]
    str2=str.replace(ele,'')

    return str2

str='i am harshal'
res=remove_index(str)
print(res)


#### Q7. Python Program to Remove the Given Key from a Dictionary



dic={1:'harshal',2:'prashant',3:'dashrath'}
def rem_key(dic):
    key=int(input("Enter key to remove:"))

    if key in dic:
        del dic[key]
        print(dic)
    else:
        print('given key is not exists in given dictionary')    


rem_key(dic)        
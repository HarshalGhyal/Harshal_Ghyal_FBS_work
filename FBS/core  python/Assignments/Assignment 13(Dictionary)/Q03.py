#### Q3. Python Program to Check if a Given Key Exists in a Dictionary or Not

def iskey_exists(dic,key):
    if key in dic:
        return f'Given key: {key} exists in given dictionary'
    else:
        return f'Given key: {key} not exists in given dictionary'


dic={'harshal':21,'pratham':22}    
res=iskey_exists(dic,'harsha')
print(res)
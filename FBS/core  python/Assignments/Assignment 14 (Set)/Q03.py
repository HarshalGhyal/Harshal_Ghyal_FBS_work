#### Q3.Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.


li=['apple banana','banana mango','apple mango']
def set_of_unique_str(li):
    li1=[]
    for words in li:
        for word in words.split(' '):
            li1+=[word]
    li1=set(li1)
    return li1      

res=set_of_unique_str(li)
print(res)
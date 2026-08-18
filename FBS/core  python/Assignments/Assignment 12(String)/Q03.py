#### Q3.Python Program to Detect if Two Strings are Anagrams.

def Anagram(str,str1):
    str=sorted(str)
    str1=sorted(str1)

    if str==str1:
       return  "given both strings are anagrams"
    else:
        return "given strings are not anagrams"  


a='listen'
b='sileny'
res=Anagram(a,b)
print(res)      

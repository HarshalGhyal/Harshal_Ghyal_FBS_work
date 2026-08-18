str='listen'
dic={}
dic2={}
for ch in str:
    if ch not in dic:
        dic[ch]=1
  

str1='silent'
for ch in str1:
    if ch not in dic2:
        dic2[ch]=1
count=0
for i in dic:
    if i not in dic2:
        count -= 1
    elif dic[i] != dic2[i]:
        count -= 1

                
if count==0:
    print(" strings are anagram!")
if count<0:
    print("strings are not anagram!")    
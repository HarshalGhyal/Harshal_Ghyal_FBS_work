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

    
if dic==dic2:
    print('anagram')
else:
    print('not anagram')    
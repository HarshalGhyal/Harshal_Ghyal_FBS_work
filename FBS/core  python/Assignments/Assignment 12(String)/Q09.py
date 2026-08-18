#### Q9.Python Program to Calculate the Number of Words and the Number of
# Characters Present in a String

def count_words_char(str):
    
    li=str.split()
    
    
    count_words=0
    count=0
    for s in li:
        count_words+=1
        for ch in s:
            # if ch!=' ':
            count+=1
    return f'The number words in given string: {count_words} \nThe number of characters in given string: {count}'    


str='harshal lives in pune'
res=count_words_char(str)
print(res)
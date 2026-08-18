#### Q8.Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary.

str='python is interpreted language python is high level languagebis python'
def frequecy_words(str):
    words=str.split()
    freq={}
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1

    print(freq)

frequecy_words(str)
            

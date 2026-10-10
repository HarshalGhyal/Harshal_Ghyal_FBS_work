#### Q6. Use a dictionary comprehension to count the length of each word
# in a sentence (take input from user)

str=input('Enter string:')
li={i:len(i) for i in str.split(' ') }

print(li)
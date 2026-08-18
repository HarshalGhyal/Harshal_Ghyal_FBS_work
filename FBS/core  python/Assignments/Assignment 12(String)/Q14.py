#### Q14. Python Program to count the occurrences of ach word in a string.

str='qwertyachmnpkzlapachxvbnrachtyuioachpqwekmachzxcv'
def count_ach(str):
    count=str.count('ach')
    return f'count of ach in string is {count}'


res=count_ach(str)
print(res)
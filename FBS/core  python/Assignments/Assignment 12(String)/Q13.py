#### Q13.Python Program to count number of digits and letters in a string.

str='harshal1920college11736'
def number_of_digits_letters(str):
    count_digit=0
    count_letter=0
    for i in str:
        if i.isnumeric():
            count_digit+=1
        elif i.isalpha():
            count_letter+=1
    return f' The number of digits: {count_digit}\n The number of letters: {count_letter}'

res=number_of_digits_letters(str)
print(res)



     

    
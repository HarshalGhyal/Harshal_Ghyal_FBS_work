#### Q1.Python Program to Replace all Occurrences of ‘a’ with $ in a String.

def replace_char(str):
    replace_var=input("Enter character or word to replace :")
    replacement_var=input("Enter replacement char or word :")

    new_str=str.replace(replace_var,replacement_var)

    return new_str

str='i am good at python'
a=replace_char(str)

print(a)

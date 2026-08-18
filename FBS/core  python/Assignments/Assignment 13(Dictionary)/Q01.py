#### Q1. Python Program to Add a Key-Value Pair to the Dictionary

def student(**args):
    dic={args["name"]:args["age"]}
    return dic

res=student(name="Harshal", age=21)
print(res)


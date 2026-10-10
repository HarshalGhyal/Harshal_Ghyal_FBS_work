#### Q3. Count the number of spaces in a string (take input from user)

string = input("Enter a string: ")

count = sum([1 for ch in string if ch == " "])

print("Number of spaces:", count)
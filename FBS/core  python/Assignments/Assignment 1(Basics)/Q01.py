#### Q1. write a program to calculate the percentage of student based on marks of any 5 subjects ?

# so we are gonna calculate percentage upon marks of 5 subjects.so lets take a total marks of 5 subjects as 500.

Total_marks=500

# now we are gonna get input from user of all obtained marks in each subjects.and each subject marks has to be smaller than or equal to 100

sub_1=int(input("enter your subject 1 marks:"))
sub_2=int(input("enter your subject 2 marks:"))
sub_3=int(input("enter your subject 3 marks:"))
sub_4=int(input("enter your subject 4 marks:"))
sub_5=int(input("enter your subject 5 marks:"))

# so now we have marks of 5 subjects obtained.lets add all 5 suject marks to get its sum.

sum_of_obtained_marks=sub_1+sub_2+sub_3+sub_4+sub_5

# so the formula for percentage is total obtained marks/total marks *100

percentage=(sum_of_obtained_marks/Total_marks)*100

#lets display the results.

print(f"the percentage of student is {percentage} %")

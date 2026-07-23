#### Q2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

#lets take input of number of students:
n_students=int(input("Enter number of students:"))

# lets initialize the var 
sum_per=0

# lets iterate:
for i in range(1,n_students+1):
    # lets take marks of 5 students each through loop.
    sub1_marks=int(input(f"subject 1 marks for student {i}:"))
    sub2_marks=int(input(f"subject 2 marks for student {i}:"))
    sub3_marks=int(input(f"subject 3 marks for student {i}:"))
    sub4_marks=int(input(f"subject 4 marks for student {i}:"))
    sub5_marks=int(input(f"subject 5 marks for student {i}:"))
    # lets calculate total obtained marks:
    sum=sub1_marks+sub2_marks+sub3_marks+sub4_marks+sub5_marks
    #lets calculate percentage
    perc=sum/500*100
    #lets print each students marks
    print(f"Student {i} percentage is {perc}%")
    # lets add all obtained percentage to calculate avg
    sum_per+=perc
else:
    #lets calculate average percentage of students
    avg=sum_per/n_students
    # lets print average percentage:
    print(f"Average percentage for given {n_students} students is {avg}%")

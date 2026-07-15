#### Q9.Input 5 subject marks from user and display grade(eg.First class,Second class ..)

#lets take input of 5 subject marks:
sub1=int(input("enter marks of subject 1:"))

sub2=int(input("enter marks of subject 2:"))

sub3=int(input("enter marks of subject 3:"))

sub4=int(input("enter marks of subject 4:"))

sub5=int(input("enter marks of subject 5:"))

total_marks=500

# lets calculate percentage
if sub1<=100 and sub2<=100 and sub3<=100 and sub4<=100 and sub5<=100:
    obt_total_marks=sub1+sub2+sub3+sub4+sub5
    obt_perc=obt_total_marks/total_marks*100
    if obt_perc>=75:
        print("\nyou got first class!")
    elif obt_perc>=60:
        print("\nyou got second class!")
    elif obt_perc>40:
        print("\nyou got third class!")
    else:
        ("\nsorry ,you have failed!")            
else:
    print("\nplease enter appropriate marks!")
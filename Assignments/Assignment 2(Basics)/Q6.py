#### Q6.WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.

# lets take basic salary as a input:

Basic_salary=float(input("Enter your basic salary:"))

# lets take da,ta and hra in percentage as given assign them variable accordingly

da=10  #so, da is 10% that is also written as 10/100.
da=10/100 

ta=12  #so, ta is 12% that is also written as 12/100.
ta=12/100

hra=15  #so, hra is 15% that is also written as 10/100.
hra=15/100

# lets calculate da, ta and hra on basic salary.

da_on_salary=Basic_salary*da

ta_on_salary=Basic_salary*ta

hra_on_salary=Basic_salary*hra

# lets calculate total salary.

Total_salary=Basic_salary+da_on_salary+ta_on_salary+hra_on_salary

#lets display the output:

print(f"For Basic Salary {Basic_salary}, DA = {da_on_salary}, TA = {ta_on_salary}, HRA = {hra_on_salary}, Total Salary = {Total_salary}")



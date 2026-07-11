#### Q4. write a program to enter P,T,R and calculate simple interest?

#before going to code what is P,T and R?
# P stands for principal(amount of money borrowed or save)
# T stands for Time(duration of loan or deposit)
# R stands for Rate(rate of interest charge per yr or given amount of time)
#lets take 1 year and its months
year=12
# lets take p first as a input

P_amount=int(input("enter principal amount:"))

# lets take time as a months.as we are taking duration in months but formula is for year input of duration we have to divde it by 12

T_time=int(input("enter your time duration in years:"))


# lets take rate of interest as a percentage

R_rate=int(input("enter rate of interest as a percentage:"))


# so the formula for simple interest is P*R*t/1000

SI=P_amount*R_rate*T_time/100


# total amount to pay after time duration is simple interest + principal

total_amt_to_pay=SI+P_amount



# lets display simple interest and total pay amount

print("The simple interest for given input is:",SI,"Rupees")
print("The total amount you have to pay after time duration is:",total_amt_to_pay,"Rupees")




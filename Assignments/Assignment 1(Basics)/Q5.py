#### Q5. write a program to enter P,T,R and calculate compound interest?

# what is compound interest?
# Compound interest is the interest on a loan or deposit calculated based on both the initial principal and the accumulated interest from previous periods. 


# lets take principal amount first as a input

P_amt=int(input("Enter the pricipal amount:"))

# now, rate of interest in %

R_interest=float(input("Enter the rate of interest:"))

# now, key part lets take n as a number of times interst is compounded per year
n=int(input("Enter the number of times interest is compounded per yr: "))

# now, Time duration in years

T=int(input("Enter the time duration in years:"))

# so the formula for final amt after compounded years is: final amount =P(1+r/n)^nt

final_amt=P_amt*(1+R_interest/100/n)**(n*T)

#so the formula for compound interst is CI=final amount - principal

CI=final_amt - P_amt

# lets display final amt and compound interst

print("The final amount after compounded interst is:",final_amt,"Rupees")
print("The compound interst is:",CI,"Rupees")


#### Q13.Write a program to input electricity unit charges and calculate total electricity bill
# according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill.

# lets take input of electricity unit as E_unit:
E_unit=int(input("Enter electricity units:"))
#lets initialize variable bill value as zero: 
bill=0
# lets check bill by if else ladder:
if E_unit<=50:
    bill=E_unit*1/2
elif E_unit<=150:
    bill=25+(E_unit-50)*0.75
elif E_unit<=250:
    bill=25+75+(E_unit-150)*1.20
elif E_unit>250:
     bill=25+75+120+(E_unit-250)*1.5

total=bill*20/100

total_bill=bill+total


print(f"for given units:{E_unit} total bill is:{total_bill} ")



               
               
        
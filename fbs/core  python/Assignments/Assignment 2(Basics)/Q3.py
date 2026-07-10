#### Q3.Convert distance given in feet and inches into meter and centimeter.

# Lets take input as distance in feet and inches.
feet=float(input("Enter distance in feet:"))
inches=float(input("Enter distance in inches:"))

#lets covert feet and inches into only inches.
total_inches=(feet*12)+inches

# lets covert inches into centimeter. where,1 inch=2.54 cm
total_cm=total_inches*2.54

#lets covert centimeter into meter.where,1m=100cm so we have to divide total cm by 100 to get meter.
total_m=total_cm/100

#lets display the output.
print(f"so, given distance in feet: {feet} and inches: {inches} is in meter:{total_m} and centimeter:{total_cm}")
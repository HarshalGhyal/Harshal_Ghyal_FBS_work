#### Q5.WAP to calculate selling price of book based on cost price and discount.

#lets take input as cost price and discount
cost_price=float(input("Enter the cost price of the book:"))

discount=float(input("Enter the discount percentage:"))

# lets calculate selling price of book

selling_price=cost_price-(cost_price*discount/100)

#lets display the output:

print(f"Cost price:{cost_price} , Discount:{discount} % ,Selling price after discount:{selling_price}")

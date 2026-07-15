#### Q6.Write a program to calculate profit or loss.

# lets take two input cost price and selliing price:
cost_price=float(input("Enter cost price(in rupees):"))

sell_price=float(input("Enter selling price(in RS):"))

if sell_price>cost_price:
    print(f'its a profit! and profit is {sell_price-cost_price} RS')
elif sell_price<cost_price:
    print(f"its a loss! and loss is {cost_price-sell_price} RS") 
else:
    print('its a tie ,neither profit nor loss!')       
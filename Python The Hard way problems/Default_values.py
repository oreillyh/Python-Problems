def subtotal(orderAmt, salesTax=0.08):
    subtotal = float(orderAmt) * (1 + float(salesTax))
    return subtotal

FirstOrderTotal = subtotal(300)
secondOrderTotal = subtotal(400, 0.06)

thirdOrderAmount = input("What was the order amount?")
thirdTax = input("Enter your sales tax rate.")
thirdOrderTotal = subtotal(thirdOrderAmount, thirdTax)
fourthOrderTotal = subtotal(800)

print("Your subtotal for the first order is %.2f" %FirstOrderTotal)
print("Your subtotal for the second order is %.2f" %secondOrderTotal)
print("Your subtotal for the third order is %.2f" %thirdOrderTotal)
print("Your subtotal for the fourth order is %.2f" %fourthOrderTotal)

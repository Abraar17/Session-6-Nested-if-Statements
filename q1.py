#The input to the problem is quantity of widgets.
quant = int( input("enter quantity: ") )


#Calculate the extended price (quantity x price). Calculate tax at 7%.

if quant > 10000:
  price = quant * 10

elif quant > 5000 or quant < 10000:
  price = quant * 20

else:
  price = quant * 30

#Display the extended price, tax amount and total.
print("extended price: ", (price))
print("tax amount: ", (price*0.07))
print("total", (price + (price * 0.07)))




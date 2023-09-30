partnum = int(input("enter partnumber: "))
quant = int(input("enter quant: "))

if partnum == 10 or partnum == 55:
  priceperpart = 1
  price = quant * priceperpart

elif partnum == 99:
  priceperpart = 2
  price = quant * priceperpart

elif partnum == 80 or partnum == 70:
  priceperpart = 3
  price = quant * priceperpart

else:
  priceperpart = 5
  price = quant * priceperpart

print("partnumber: ", partnum)
print("priceperpart: ", priceperpart)
print("total cost: ", price)

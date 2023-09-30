numoftix = int(input("Enter number of concert tickets: "))

if numoftix >= 25:
    priceperticket = 50
    cost = numoftix * priceperticket

elif numoftix <= 24 and numoftix >= 10:
    priceperticket = 60
    cost = numoftix * priceperticket

elif numoftix <= 9 and numoftix>= 5:
    priceperticket = 70
    cost = numoftix * priceperticket

else:
  priceperticket = 75
  cost = numoftix * priceperticket


print("Number of ticket: ", numoftix)
print("Price per ticket: ", priceperticket)
print("Total cost: ", cost)


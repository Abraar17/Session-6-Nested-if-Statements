principle = float(input("Enter principle amount: "))
yearstoMat = int(input("Enter the years to maturity: "))

if principle > 100000:
  if yearstoMat >= 5:
    interest = 0.06
elif 50000 <= principle <= 100000:
  if yearstoMat == 10:
    interest = 0.05
  elif yearstoMat == 5:
    interest = 0.04
else:
  interest = 0.02

finalInterest = principle * interest

print("Principle: ", principle)
print("Interest Rate: ", interest * 100)
print("Interest amount for the year 1: ", finalInterest)

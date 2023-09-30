lastname = input("enter last name: ")
salary = float(input("enter salary: "))
joblvl = int(input("enter job level: "))

if joblvl >= 10:
  bonrate = 0.25
  bonus = salary * bonrate

elif joblvl <= 9 and joblvl >= 5:
  bonrate = 0.20
  bonus = salary * bonrate
  
else:
  bonrate = 0.10
  bonus = salary * bonrate

print("lastname: ", lastname)
print("bonus: ", bonus


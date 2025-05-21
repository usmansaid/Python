amount = float(input("Enter the decimal number: "))

totalCents = round(amount * 100)

# For obtaining dollars
dollars = totalCents // 100
print("Dollars are: " + str(dollars))
totalCents %= 100

# For Quarters
quarters = totalCents // 25
print("Quarters are: " + str(quarters))
totalCents %= 25

# For Dimes
dimes = totalCents // 10
print("Dimes are: " + str(dimes))
totalCents %= 10

# For Nickels
nickels = totalCents // 5
print("Nickels are: " + str(nickels))
totalCents %= 5

# For Remaining Pennies
print("Pennies are: " + str(totalCents))
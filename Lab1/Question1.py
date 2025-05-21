hourlyRate = float(input("Enter your actual hourly rate: "))
hoursWorked = float(input("Enter the hours you worked: "))

if hoursWorked <= 40:
    totalWages = hoursWorked * hourlyRate
    print("Your total wage is: $" + str(totalWages))

elif hoursWorked > 40:
    totalWages = (40 * hourlyRate) + (hoursWorked - 40) * hoursWorked * 1.5
    print("Your total wage with overtime pay is: $" + str(totalWages))
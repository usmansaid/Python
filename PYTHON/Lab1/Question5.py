totalMinutes = int(input("Enter the minutes: "))

hours = int(totalMinutes / 60)
minutes = int(totalMinutes % 60)

print("Now the time is: " + str(hours) + ":" + str(minutes))

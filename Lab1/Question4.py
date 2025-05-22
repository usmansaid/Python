studentsA = int(input("Enter the number of students in Class A: "))
studentsB = int(input("Enter the number of students in Class B: "))
studentsC = int(input("Enter the number of students in Class C: "))
totalStudents = studentsA + studentsB + studentsC

desksA = int((studentsA + 1) / 2)
desksB = int((studentsB + 1) / 2)
desksC = int((studentsC + 1) / 2)

totalDesks = desksA + desksB + desksC
print("Total Desks required are: " + str(totalDesks))
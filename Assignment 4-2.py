#Declarations
prodScore = 0
employeeBonus = 0.00

employeeName = input("Enter Employee Name: ")
shifts = int(input("Enter number of shifts: "))
transactions = int(input("Enter number of transactions: "))
transAmount = float(input("Enter transactions dollar value: "))

prodScore = (transAmount / transactions) / shifts

if prodScore <= 30:
    employeeBonus = 50.00
elif prodScore >= 31 and prodScore <= 69:
    employeeBonus = 75.00
elif prodScore >= 70 and prodScore <= 199:
    employeeBonus = 100.00
elif prodScore >= 200:
    employeeBonus = 200.00

print("Employee Name: " + employeeName)
print("Employee Bonus: $" + str(employeeBonus))
number_of_days = int(input("Enter number of days: "))

years = number_of_days // 365

months = (number_of_days % 365) //7

days = (number_of_days - years % 365) %7

print("Years = ", years)
print("Months = ", months)
print("Days = ", days)